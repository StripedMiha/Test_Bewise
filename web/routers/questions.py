from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy import desc, select
from sqlalchemy.orm import Session

from external.question_source import get_questions
from db.tables import Question
from db.db_connection import get_session


router = APIRouter()


async def check_question(list_id: list[int], question: dict) -> Question:
    if question.get('id') in list_id:
        new_question: dict = get_questions(1)
        return check_question(list_id, new_question)
    else:
        return Question(question=question.get('question'),
                        answer=question.get('answer'),
                        category_id=question.get('category_id'),
                        create_date=question.get('created_at'),
                        added_date=datetime.now(),
                        question_id=question.get('id'))


@router.post("/quest", response_model=Optional[Question])
async def add_questions(questions_num: int = 1, session: Session = Depends(get_session)):
    result = session.execute(select(Question).order_by(desc(Question.added_date)))
    last_questions: Optional[Question] = result.scalars().first()
    while questions_num > 0:
        questions: list[dict] = await get_questions(questions_num)
        result = session.execute(select(Question.question_id))
        questions_id: list[int] = result.scalars().all()
        for question in questions:
            checked_question: Question = await check_question(questions_id, question)
            session.add(checked_question)
        session.commit()
        questions_num -= len(questions)
    return last_questions
