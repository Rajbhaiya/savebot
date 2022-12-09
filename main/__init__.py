#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "13675555"
API_HASH = "c0da9c346d2c45dbc7ec49a05da9b2b6"
BOT_TOKEN = "5555986769:AAG-nNw82PHwBPlPZ5h55d3hnfHxzqc5JeI"
SESSION = "AQB05XzRIbT1KA5wU3OK0Opiih0xa-Rri-b4-uotETHSTF_wg1BeWqbxx1WF1tIu_OLZ8HemRl8gbPphaPR2oajECUdEveliWSXAlLbWWS9AfCNHwo_3ijCX_C14QSh5Np9PNhyThR6RU-DzA99hgQ-iOF9pGuxBU5NVMlo1PE7K55Q6BTklPS0Zs3G01KdjYPYuraM7fJQhmwmLKD-Mrrfpo6ZJeRsAbneWL_WKWlpAJXyK0nAeUJyIWSDO7RfkP5-Z3qXM8xSfsIHbAbmqnV22q-TuNrxJI1Dt_aJHJ8D-KZbX2-kjNKd-QIlYpBIX3VFDKU6TiQuNVykn5fIRm-haAAAAATerd_sA"
FORCESUB = "Ecchi_world_K"
AUTH = "5591954930"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
