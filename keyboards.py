from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from configs import LANGUAGES

def language_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = []
    for lang in LANGUAGES.values():
        btn = KeyboardButton(text=lang)
        buttons.append(btn)

    markup.add(*buttons)
    return markup


