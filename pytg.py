import logging
from telegram import Update, Bot
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Replace with your token
TOKEN = "5386670063:AAEM8nOGZqJ7N7OkUGoNP9o-xiftgQhGux8"
MAIN_CHANNEL_ID = -1001208594988
CHANNELS = [-1001296393536, -1001207248779, -1001318277713, -1001166047824, -1001308597555]

# Command handler for /start and /help commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id, "**You Have No Permission to use this!**", parse_mode=ParseMode.MARKDOWN)

# Message handler for forwarding channel posts
async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message or update.channel_post

    if message is None:
        logger.warning(f"Update without message or channel_post received: {update}")
        return
    
    if message.chat.id == MAIN_CHANNEL_ID:
        for channel_id in CHANNELS:
            try:
                await context.bot.copy_message(chat_id=channel_id, from_chat_id=MAIN_CHANNEL_ID, message_id=message.message_id)
            except Exception as e:
                logger.error(f"Failed to forward message from {MAIN_CHANNEL_ID} to {channel_id}: {e}")

def main() -> None:
    # Create the Application and pass it your bot's token
    application = ApplicationBuilder().token(TOKEN).build()

    # Command handler for /start and /help
    application.add_handler(CommandHandler(["start", "help"], start, filters=filters.ChatType.PRIVATE))

    # Message handler for forwarding messages and channel posts
    application.add_handler(MessageHandler(filters.TEXT | filters.PHOTO | filters.Document.ALL | filters.ChatType.CHANNEL, forward_message))

    # Run the bot
    application.run_polling()

if __name__ == '__main__':
    main()
