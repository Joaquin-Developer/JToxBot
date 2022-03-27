import os

TOKEN = "..."  # Poner el token
URL = "https://api.telegram.org/bot" + TOKEN + "/"

API_KEY = os.environ["PYOWN_API_KEY"]


CITIES_JSON_ROUTE = os.environ["PP_ROUTE"] + "/BOT_Telegram_Python/v2.0/data/city_list.json"
