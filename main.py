import time
from telethon.sync import TelegramClient, events
from telethon.tl.types import User

api_id = 16042035
api_hash = "2b7616c04482d21542d546be1b8dec48"

phone = "+447828387395" # your phone
username = "main"
source_channel_id = 5286195203

client = TelegramClient(username, api_id, api_hash)
client.start()

timer_is_active = True



def countdown():
    global client
    global timer_is_active

    s = 60

    while s:
        print(s)
        time.sleep(1)
        s -= 1

        
    try:
        for dialog in client.iter_dialogs():
            if dialog.id == source_channel_id:
                 response = client.send_message(dialog.id, "🎉 Bonus")
                 print(response.date)

    except Exception as e:
        print(e)

    countdown()



countdown()
client.run_until_disconnected()