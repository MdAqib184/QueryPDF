from sqlalchemy import Column, Integer, String, Text, DateTime, func
from .database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    content = Column(Text)
    uploaded_at = Column(DateTime, default=func.now())
