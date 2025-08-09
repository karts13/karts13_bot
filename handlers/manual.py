# handlers/help.py
from telegram import Update
from telegram.ext import ContextTypes

HELP_TEXT = (
    "📚 *What you can do:*\n\n"
    "• /add - Quickly add a movie/show to your list\n"
    "• /list - View your movies/shows with filters\n"
    "• /remove - Remove a movie/show from your watchlist\n"
    "• /manual - Need a hand? Get this message again\n\n"
    "Just type a command or tap a button to get started! 🎉"
)

async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_TEXT, parse_mode="Markdown")