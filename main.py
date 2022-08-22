import telebot
import random

API_KEY = "5729641344:AAHo-ghSD97FFEEu0W1GeWVjuWvvxRtMphw"
bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=["Hi"])
def hi(message):
    if a==1:
        bot.reply_to(message, "You are Fat 1")
    elif a==2:
        bot.reply_to(message, "You are Fat 2")
    elif a==3:
        bot.reply_to(message, "You are Fat 3")

    elif a==4:
        bot.reply_to(message, "You are Fat 4")

    elif a==5:
        bot.reply_to(message, "You are Fat 5")
    elif a==6:
        bot.reply_to(message, "You are Fat 6")
    elif a==7:
        bot.reply_to(message, "You are Fat 7")
    elif a==8:
        bot.reply_to(message, "You are Fat 8")
    elif a==9:
        bot.reply_to(message, "You are Fat 9")

    elif a==10:
        bot.reply_to(message, "You are Fat 10")
#     bot.reply_to(message, "pooarasu loves priyanka mohan")

# @bot.message_handler(commands=["insult"])
# a = random.randrange(1,10,1)
# def insult(message):
#     if a==1:
#         bot.reply_to(message, "You are Fat 1")
#     elif a==2:
#         bot.reply_to(message, "You are Fat 2")
#     elif a==3:
#         bot.reply_to(message, "You are Fat 3")

#     elif a==4:
#         bot.reply_to(message, "You are Fat 4")

#     elif a==5:
#         bot.reply_to(message, "You are Fat 5")
#     elif a==6:
#         bot.reply_to(message, "You are Fat 6")
#     elif a==7:
#         bot.reply_to(message, "You are Fat 7")
#     elif a==8:
#         bot.reply_to(message, "You are Fat 8")
#     elif a==9:
#         bot.reply_to(message, "You are Fat 9")

#     elif a==10:
#         bot.reply_to(message, "You are Fat 10")

bot.polling()