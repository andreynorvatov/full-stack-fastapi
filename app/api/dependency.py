from app.core.db import engine, SessionLocal
from sqlalchemy.orm import Session



def get_db():
    with Session(engine) as session:
        yield session

    # return SessionLocal
