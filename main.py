import os
import time
import telebot
import requests
import json
import random

API_KEY = "5729641344:AAHo-ghSD97FFEEu0W1GeWVjuWvvxRtMphw"
print(API_KEY)
bot = telebot.TeleBot(API_KEY)
print("Logged")


def splitter(msg):
    for test in msg:
        if "@" in test:
            return test

def for_gif(msg):
    for dollar in msg:
        if "$" in dollar:
            return dollar

def getGifUrl(search_term):
    print("Entered")
    apikey = "AIzaSyB6LQderKit11_1xdLeeeT-S7mYzBGzPSY"  # test value
    lmt = 10
    ckey = "TELebot"
    # get the top 8 GIFs for the search term
    r = requests.get("https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" % (search_term, apikey, ckey,  lmt))
    ind = random.randint(0,10)
    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_8gifs = json.loads(r.content)
        outputGif = top_8gifs['results'][ind]['media_formats']['tinygif']['url']
        return outputGif
    else:
        top_8gifs = None
        return top_8gifs


@bot.message_handler(commands=["start"])
def hi(message):
     bot.reply_to(message, "Welcome to our Bot")



@bot.message_handler(commands=["greet"])
def greeting(message):  
    bot.reply_to(message, "Hello, How are you?")


@bot.message_handler(func=lambda msg: msg.txt is not None and '$' in msg.text)
def gifs(message):
    gif_text = for_gif(message)
    search_ele = gif_text[1:]
    print(search_ele)
    gif = getGifUrl(search_ele)
    bot.reply_to(message, gif)

 
@bot.message_handler(commands=["help"])
def helping(message):
    bot.reply_to(message, """ There are few commands available in this bot.
    /start - to start the bot
    /greet - to get greetings
    $(gifname) - to get a gif of the message
    @(user_name) - to get the insta profile link """)


@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
def insta_profile(message):
    texts = message.text.split()
    calling = splitter(texts)
    bot.reply_to(message, "https://instagram.com/{}".format(calling[1:]))


@bot.message_handler(func=lambda m: True)
def repeat(message):
    bot.send_message(message.chat.id, message.text)


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(1)

