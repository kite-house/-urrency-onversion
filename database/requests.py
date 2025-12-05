from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from database.models import Base, Course, DateUpdate, datetime
from dotenv import get_key

engine = create_async_engine(url = get_key('.env', 'DATABASE'))

async_session = async_sessionmaker(engine)

async def async_main() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def write_courses(rates: dict) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Course.metadata.drop_all)
        await conn.run_sync(Course.metadata.create_all)

    async with async_session() as session:
        courses = [
            Course(code=code, value=value) for code, value in rates.items()
        ]
        session.add_all(courses)
        
        session.add(DateUpdate(
            date_update = datetime.now()
        ))

        await session.commit()