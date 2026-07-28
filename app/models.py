from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database import Base


class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    name = Column(String)
    contact = Column(String)
    source = Column(String)
    comment = Column(String)