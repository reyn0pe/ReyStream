import time
import pytz
import asyncio
import time
import uvloop
import importlib
from pytz import utc
from pyrogram import Client
from Music.config import AUTO_LEAVE
from Music.config import API_ID, API_HASH, BOT_TOKEN, MONGO_DB_URI, SUDO_USERS, LOG_GROUP_ID
from Music import BOT_NAME, ASSNAME, app, client
from Music.MusicUtilities.database.functions import clean_restart_stage
from Music.MusicUtilities.database.queue import (get_active_chats, remove_active_chat)
from Music.MusicUtilities.tgcallsrun import run
from pytgcalls import idle
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from Music.MusicUtilities.helpers.autoleave import leave_from_inactive_call
from apscheduler.schedulers.asyncio import AsyncIOScheduler


scheduler = AsyncIOScheduler()

Client(
    ':Music:',
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins={'root': 'Music.Plugins'},
).start()


print(f"[INFO]: BOT MULAI SEBAGAI {BOT_NAME}!")
print(f"[INFO]: ASISTEN MULAI SEBAGAI {ASSNAME}!")



async def load_start():
    restart_data = await clean_restart_stage()
    if restart_data:
        print("[INFO]: MENGIRIM RESTART STATUS KE SERVER")
        try:
            await app.edit_message_text(
                restart_data["chat_id"],
                restart_data["message_id"],
                "**Restart Bot Berhasil.**",
            )
        except Exception:
            pass
    served_chats = []
    try:
        chats = await get_active_chats()
        for chat in chats:
            served_chats.append(int(chat["chat_id"]))
    except Exception as e:
        print("Terjadi kesalahan saat membersihkan db")
    for served_chat in served_chats:
        try:
            await remove_active_chat(served_chat)                                         
        except Exception as e:
            print("Terjadi kesalahan saat membersihkan db")
            pass     
    await app.send_message(LOG_GROUP_ID, "Bot Dimulai")
    print("[INFO]: MEMULAI BOT DAN MENGIRIM INFO KE SERVER")
    if AUTO_LEAVE:
        print("[ INFO ] JADWAL MULAI")
        scheduler.configure(timezone=pytz.utc)
        scheduler.add_job(
            leave_from_inactive_call, "interval", seconds=AUTO_LEAVE
        )
        scheduler.start()    
    
   
loop = asyncio.get_event_loop()
loop.run_until_complete(load_start())

run()
idle()
loop.close()

print("[LOG] MENUTUP BOT")