from pyrogram import Client, filters, handlers
import logging
import os
import requests

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# TOKEN = os.getenv("TOKEN")
TOKEN = "5386670063:AAEM8nOGZqJ7N7OkUGoNP9o-xiftgQhGux8"
main_channel = -1001208594988

# -1001296393536
# -1001208594988
# -1001207248779
# -1001318277713

# -1001308597555
# -1001207248779
# -1001318277713
# -1001166047824
# # -1001208594988
# -1001296393536
CHANNELS = [-1001296393536,-1001207248779,-1001318277713,-1001166047824,-1001308597555]

app = Client(
    "my_account",
    api_id=1472621,
    api_hash="188e8b4d277a61fe4bef4a7b6f2fa4bb",
    bot_token=TOKEN
)

@app.on_message(filters.command(["start", "help"]) & filters.private)
def start(client, message):
    chat_id = message.from_user.id
    app.send_message(chat_id, "**You Have No Permission to use this!**")

@app.on_message(filters.text | filters.photo | filters.document)
def main(client, message):
    if message.chat.id == main_channel:
            for channel in CHANNELS:
            	app.copy_message(channel, main_channel, message.id)

app.add_handler(handlers.MessageHandler(start, filters.command(
    ["start", "help"]) & filters.private))
app.add_handler(handlers.MessageHandler(main, filters.text | filters.photo | filters.document))
app.run()
