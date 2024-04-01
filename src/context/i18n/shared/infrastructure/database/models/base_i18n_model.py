from sqlalchemy import Column, DateTime
from sqlalchemy.orm import DeclarativeBase


class BaseI18nModel(DeclarativeBase):
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)
