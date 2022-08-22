import telebot
import random

API_KEY = "5729641344:AAHo-ghSD97FFEEu0W1GeWVjuWvvxRtMphw"
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=["start"])
def hi(message):
     bot.reply_to(message, "Welcome! \nUse /help to find How to use the Bot!")

@bot.message_handler(commands=["help"])
def helping(message):
    bot.reply_to(message, "To use this, You need to verify your username")


while True:
    try:
        bot.polling()
    except Exception:
        bot.sleep(5)
