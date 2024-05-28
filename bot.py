from telethon.sync import TelegramClient, events
from telethon.tl.functions.messages import ForwardMessagesRequest

api_id = ''  # Sostituisci con il tuo API ID
api_hash = ''  # Sostituisci con il tuo API Hash
phone = '+39'  # Sostituisci con il tuo numero di telefono

client = TelegramClient(phone, api_id, api_hash)
client.start()

@client.on(events.NewMessage())
async def my_event_handler(event):
    if event.chat_id == -1002156859695:
        await event.forward_to(-1002241933046) 

client.run_until_disconnected()
