# TEAM RISHU ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "20137303"
    API_HASH = "d1a8a231897f62d26a8cf9974b1303f8"  
    TOKEN = os.environ.get("TOKEN", "YOUR BOT TOKEN")
    MONGO_URL = "mongodb+srv://sevexedits:5JyQbk44RuB2jQj6@cluster0.lezcv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    START_PIC = "https://files.catbox.moe/z2ajhe.jpg"
    SUDOERS = filters.user(["YOUR OWNER ID"])
