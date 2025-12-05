from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy import String
from datetime import datetime

class Base(AsyncAttrs, DeclarativeBase):
    pass

class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(50))
    value: Mapped[float] # К USD
 
class DateUpdate(Base):
    __tablename__ = 'DateUpdates'

    id: Mapped[int] = mapped_column(primary_key=True)
    date_update: Mapped[datetime]


