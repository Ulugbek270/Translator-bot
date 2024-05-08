#  pip install pyTelegramBotApi

from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardRemove
from keyboards import language_btn
from googletrans import Translator
from configs import get_key

TOKEN = '6323073772:AAFIvXK-zTl0uY02Xne8PbGcaIQ63v04C8E'

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'about', 'help', 'history'])
def command_start(message: Message):
    chat_id = message.chat.id
    username = message.from_user.username
    if message.text == '/start':
        bot.send_message(chat_id, f'Привет {username} я твой Бот переводчик')
        confirm_src_asc_dest(message)
    elif message.text == '/about':
        bot.send_message(chat_id, 'Данный бот переводчик может переводить с русского на выбранный вами язык')
    elif message.text == '/help':
        bot.send_message(chat_id, 'Если у вас проблемы с ботом напишите разработчику @Kazus92')
    elif message.text == '/history':
        bot.send_message(chat_id, 'История пока не работает')


def confirm_src_asc_dest(message: Message):
    chat_id = message.chat.id
    text_src = 'Русский'
    msg = bot.send_message(chat_id, 'Выбери на какой язык перевести', reply_markup=language_btn())
    bot.register_next_step_handler(msg, confirm_dest_asc_src, text_src)


def confirm_dest_asc_src(message, text_src):
    chat_id = message.chat.id
    text_dest = message.text
    if text_dest == '/start' or text_dest == '/help' or text_dest == '/about' or text_dest == '/history':
        command_start(message)
    else:
        msg = bot.send_message(chat_id, 'Введите текст для перевода: ', reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, confirm_text_translate, text_src, text_dest)


def confirm_text_translate(message, text_src, text_dest):
    chat_id = message.chat.id
    text_trans = message.text
    if text_trans == '/start' or text_trans == '/help' or text_trans == '/about' or text_trans == '/history':
        command_start(message)
    else:
        teacher = Translator()
        msg = teacher.translate(text=text_trans, src=get_key(text_src), dest=get_key(text_dest) ).text
        bot.send_message(chat_id, msg)

        new_msg = bot.send_message(chat_id, 'Введите слово или текст который хотите перевести или выберите другую команду')
        bot.register_next_step_handler(new_msg, confirm_text_translate, text_src, text_dest)




bot.infinity_polling()
