from time import time
import telebot
import random

API_KEY = "5729641344:AAHo-ghSD97FFEEu0W1GeWVjuWvvxRtMphw"
bot = telebot.TeleBot(API_KEY)

def splitter(msg):
    for test in msg:
        if "@" in test:
            return test


@bot.message_handler(commands=["start"])
def hi(message):
     bot.reply_to(message, "Welcome! \nUse /help to find How to use the Bot!")

@bot.message_handler(commands=["help"])
def helping(message):
    bot.reply_to(message, "To use this, You need to verify your username")

@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
def insta_profile(message):
    texts = message.split()
    calling = splitter(texts)

    bot.reply_to(message, "https://instagram.com/{}".format(calling[1:]))


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(5)
