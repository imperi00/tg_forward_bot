# -*- coding: utf-8 -*-
from telethon import TelegramClient, events

# === ��������� ===

api_id = 27496680     # ? ������ ���� API ID
api_hash = '89d47466390947e9ee9d3792a5536b52'  # ? ������ ���� API HASH
session_name = 'forward_session'  # ��� ����� ������ (����� �����)

# �������� � ��������� ����� (����� username ��� -100xxxxxxxxxx)
source_channel = -1002666896971   # ? �������� �� ID ��� username ������
# test source_channel = -1002872072610   # ? �������� �� ID ��� username ������
# ���� � ������ ��� �����, ���� ����������
target_chat = -4975465110      # ? �������� �� ID ������/������

# === ������������� ===

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
