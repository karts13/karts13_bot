import logging # for debugging and error logs
from telegram.ext import MessageHandler, filters, Application, CommandHandler #handles commands
from config import BOT_TOKEN
from db import init_db
from handlers.start import start_command
from handlers.manual import help_handler

# logs to teh console
logging.basicConfig(level=logging.INFO)

def main():
    init_db()  # create database bfr bot starts

    app = Application.builder().token(BOT_TOKEN).build() #creates a new instance

    # Handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex('^(/manual)$'), help_handler))

    app.run_polling() # check continously for new updates/mesg 

if __name__ == "__main__":
    print("Bot is running...")
    main()
