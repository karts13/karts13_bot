# handlers/start.py
from telegram import Update
from telegram.ext import ContextTypes
from db import add_user, get_user
from keyboards import main_menu_keyboard

BOT_NAME = "mySlate 🎬"
TAGLINE = "Chalk your slate with Movies & Shows 🎥"

DESCRIPTION = (
    "Easily track, organize, and manage your movies and TV shows with watchlists and categories.\n\n"
    "Ready to begin? 🤩 Use the menu to explore all options and usage tips!"
)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    # register user if not exists
    if not get_user(user.id):
        add_user(user.id, user.username, user.first_name)

    intro_text = (
        f"👋 Hey {user.first_name}!\n\n"
        f"Welcome to *{BOT_NAME}*\n"
        f"_{TAGLINE}_\n\n"
        f"{DESCRIPTION}"
    )

    await update.message.reply_text(intro_text, parse_mode="Markdown", reply_markup=main_menu_keyboard())