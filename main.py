from fastapi import FastAPI
import asyncio
import uvicorn

from src.scheduler import lifespan
from database.requests import async_main

app = FastAPI(
    title = 'CurrencyConversion',
    description= "API for working with currency exchange rates",
    root_path="/api/v1",
    lifespan=lifespan
)


...




if __name__ == "__main__":
    asyncio.run(async_main())
    uvicorn.run('main:app', reload=True)