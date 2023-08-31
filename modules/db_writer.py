from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, DateTime, Integer, String

DB_URL = "sqlite:///demo200_db.sqlite3"

engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    author = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created = Column(DateTime, nullable=False)

Base.metadata.create_all(bind=engine)

@contextmanager
def __get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def write(parsed_data: list):
    "Writes the parsed data to the `demo200_db.sqlite3` file."
    with __get_db() as db:
        for item in parsed_data:
            db.add(Comment(**item))
        db.commit()