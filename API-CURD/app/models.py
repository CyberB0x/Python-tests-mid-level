# app/models.py
from sqlalchemy import Column, Integer, String
from .database import Base

# SQLAlchemy модель таблицы "notes"
class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
