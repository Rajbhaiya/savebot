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
SESSION = "AQEir-kASbUYCmVeUZgU973SyYD1TRHhULlp2mBdFOsXNM0owlaj-HJEoIcJONU65BBzoU-l4V7LE6rTB11K9pB51ZYtSC_t9j5gg4_ZxUgqSXJJsGVVxPMk3lQLfRNPM65ub0ZxFIsbEivYPQCsAg4B5bNFdbVsjVyKK_2vm28UcYoh_OTud0DVYFFqdiKGRZZoDoGRtnEOalOOaPb5J63SK6hifqnqLhLkooSS5uOPpEPk1zntXRGFyVwGNjdxLavhFYNe8FjPiqrco8c1DWD6pbQXOwr8xm6cEyie_3UKku6h74XqxZ1rPqZGrF-qzqMyRmmQP-xLH9O_pyIyyxm7-JdcGAAAAAE5ARlCAA"
FORCESUB = "manga_universe"
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
