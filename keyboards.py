# keyboards.py
from telegram import ReplyKeyboardMarkup

def main_menu_keyboard():
    return ReplyKeyboardMarkup(
        [["/add", "/list"], ["/remove", "/manual"]], # row-wise
        resize_keyboard=True, # adjust the buttons
        one_time_keyboard=False, # dont hide
    )