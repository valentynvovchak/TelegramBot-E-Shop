import telebot
import time
from const import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Hello my friend, How\'re u doing?')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(text=message.text, chat_id=message.chat.id)


bot.infinity_polling()

