from sqlalchemy.orm import DeclarativeMeta, declarative_base
from pydantic import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean

# Base: DeclarativeMeta = declarative_base()


class Service(BaseModel):
    __tablename__ = "service"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    enabled = Column(Boolean, nullable=False, default=False)
