from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from contextlib import asynccontextmanager
from fastapi import FastAPI

from .request_external_api import get_rates

scheduler = AsyncIOScheduler()

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        scheduler.add_job(
            get_rates,
            trigger=IntervalTrigger(minutes=1),
            id='currency_update_job',
            replace_existing=True
        )
        scheduler.start()
        yield
    except Exception:
        pass

    finally:
        scheduler.shutdown()


















'''

API_KEY_COURS = get_key(".env", "API_KEY_COURS")
BASE_URL = "https://api.unirateapi.com/api"


@app.task()
def get_rates():
    response = requests.get(
        url = f'{BASE_URL}/rates',
        params = {
            'api_key': API_KEY_COURS
        }
    )
    with open('D:/СurrencyСonversion/src/rates_response.json', 'w') as f:
        f.write(response.json())

'''