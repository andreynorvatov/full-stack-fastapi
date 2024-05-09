from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
engine = create_engine("sqlite:///./super_duper.db", connect_args={"check_same_thread": False})
# engine = create_engine("sqlite:///./super_duper.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
