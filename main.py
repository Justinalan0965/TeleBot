import telebot

API_KEY = "5729641344:AAHo-ghSD97FFEEu0W1GeWVjuWvvxRtMphw"
bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=["Hi"])
def hi(message):
    bot.reply_to(message, "Suck my Chicken!")

bot.polling()