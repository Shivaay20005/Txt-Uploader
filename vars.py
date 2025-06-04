#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "29473197"))
API_HASH = environ.get("API_HASH", "182c589126cae7e6128a63a5c0fd40d8")
BOT_TOKEN = environ.get("BOT_TOKEN", "7776221405:AAHwFNJ6KMp3T9Z3Di_een9o4Bx6rN3izr0")
OWNER = int(environ.get("OWNER", "1511571370"))
CREDIT = "𝄟⃝‌🐬Shivaay𝄟⃝🐬"
AUTH_USER = os.environ.get('AUTH_USERS', '1511571370').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
