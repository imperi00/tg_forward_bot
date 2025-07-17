# -*- coding: utf-8 -*-
from telethon import TelegramClient, events

# === Ќј—“–ќ… » ===

api_id = 27496680     # ? ¬—“ј¬№ —¬ќ… API ID
api_hash = '89d47466390947e9ee9d3792a5536b52'  # ? ¬—“ј¬№ —¬ќ… API HASH
session_name = 'forward_session'  # им€ файла сессии (можно любое)

# »сточник Ч приватный канал (можно username или -100xxxxxxxxxx)
source_channel = -1002666896971   # ? «аменить на ID или username канала
# test source_channel = -1002872072610   # ? «аменить на ID или username канала
# ÷ель Ч группа или канал, куда пересылать
target_chat = -4975465110      # ? «аменить на ID группы/канала

# === »Ќ»÷»јЋ»«ј÷»я ===

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def forward_handler(event):
    try:
        await client.send_message(target_chat, event.message)
        print(f"Forwarded message: {event.message.id}")
    except Exception as e:
        print(f"Error forwarding message: {e}")

print("Bot started. Waiting for new messages...")

client.start()
client.run_until_disconnected()
