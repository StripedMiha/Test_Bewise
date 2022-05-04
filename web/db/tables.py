from datetime import datetime

from sqlmodel import SQLModel, Field

from .db_connection import engine


class QuestionBase(SQLModel):
    question: str
    answer: str
    category_id: int
    create_date: datetime
    added_date: datetime = datetime.now()


class Question(QuestionBase, table=True):
    __tablename__ = "questions"
    question_id: int = Field(primary_key=True)


def init_db():
     SQLModel.metadata.create_all(engine)
