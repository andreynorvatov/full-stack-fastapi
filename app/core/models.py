from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean

# Base = declarative_base()
from .db import Base

class Services(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    is_active = Column(Boolean(), nullable=False, default=True)

