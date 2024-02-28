

from django.conf import settings
import requests

def message_sender(chat_id, text):
    url = settings.TELEGRAM_BOT_URL + "sendMessage"
    data = {"chat_id": chat_id, "text": text}  
    response = requests.post(url, json=data)

