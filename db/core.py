import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import Generator

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://tasker_user:superuser_password@localhost:5432/tasker_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db() -> Generator[SessionLocal, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
