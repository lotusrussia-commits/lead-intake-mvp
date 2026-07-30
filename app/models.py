from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.database import Base


class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    name = Column(String, nullable=False)
    contact = Column(String, nullable=False)
    source = Column(String, nullable=False)
    comment = Column(String, nullable=False)
