from telethon.sync import TelegramClient

api_id = 27496680
api_hash = '89d47466390947e9ee9d3792a5536b52'

with TelegramClient('forward_session', api_id, api_hash) as client:
    for dialog in client.iter_dialogs():
        print(f"{dialog.name}: {dialog.id}")
