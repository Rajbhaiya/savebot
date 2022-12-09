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
SESSION = "AQBHfvhz_GMIwsKIfOn_KYlptj5dx1Wtj4b8vBjM4lNkVsFQRiEVCMeADnURo2Rha7x9gutooWTeUwgmdjx0_IlxgBwrmvVoFH6dO_CVtRTESnkWBPt3LfWhdOZSu-338WQ5OCbm_wP3Sx8xfmpgkqzHVUScmTvCmIp5TH0DA766QDunwoKrUgYIS-GicjgHJWiemUZJVb96D0Ygo0HzAUGTspLQSUtY4_fAVXvwNY_R8MhfhdR7DXEfuAWinVmJ5P9MO9bqohsTl01y1x60_iZb6RW8LPBMSInH8w7Lr2jAVMEAd-xqpQh9yih1lKC5NSF4WbRhfYMJG5TTjvWkUJj9AAAAATkBGUIA"
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
