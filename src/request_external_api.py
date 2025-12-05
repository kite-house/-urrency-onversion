from database.requests import write_courses
from dotenv import get_key
import requests

API_KEY_COURS = get_key(".env", "API_KEY_COURS")
BASE_URL = "https://api.unirateapi.com/api"

async def get_rates():
    response = requests.get(
        url = f'{BASE_URL}/rates',
        params = {
            'api_key' : API_KEY_COURS
        }
    )

    if response.status_code == 200:
        rates = response.json()['rates']
        if len(rates) > 1:
            await write_courses(rates)
        else:
            raise ValueError('The external service sent empty data')
    else:
        raise requests.exceptions.ConnectionError("Couldn't contact the external API")

