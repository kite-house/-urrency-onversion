from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy import delete
from models import Base, Course, DateUpdate, datetime
from dotenv import get_key

engine = create_async_engine(url = get_key('.env', 'DATABASE'))

async_session = async_sessionmaker(engine)

async def async_main() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def write_courses(rates: dict) -> None:
    async with async_session() as session:
        await session.execute(delete(Course))  

        session.add_all([
            Course(code=code, value=value) for code, value in rates.items()
        ])

        session.add(DateUpdate(
            date_update = datetime.now()
        ))

        await session.commit()
