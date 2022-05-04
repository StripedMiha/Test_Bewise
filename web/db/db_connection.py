import os

from sqlmodel import create_engine, SQLModel, Session

path = os.getenv("POSTGRES_PASSWORD_FILE")
with open(path, 'r') as inf:
    DB_PASSWORD = inf.read()
DATABASE_URL = f"postgresql+psycopg2://postgres:{DB_PASSWORD}@postgres_container/test_bewise"

engine = create_engine(DATABASE_URL, echo=True)


# def init_db():
#     SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
