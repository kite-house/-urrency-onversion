from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging

from .request_external_api import get_rates

scheduler = AsyncIOScheduler()
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        scheduler.add_job(
            get_rates,
            trigger=IntervalTrigger(minutes=30),
            id='currency_update_job',
            replace_existing=True
        )
        scheduler.start()
        yield
        logger.info('Currency exchange rate data was successfully updated automatically via the task scheduler')

    except Exception as error:
        logger.error(f'An error has occurred in the scheduler:: {error}')

    finally:
        scheduler.shutdown()















