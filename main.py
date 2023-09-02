import time
import telebot
import requests
import json
import random
import API_KEY
import pyqrcode


print(API_KEY.BOT_KEY)
bot = telebot.TeleBot(API_KEY.BOT_KEY)
print("Logged")


def splitter(msg):
    for test in msg:
        if "@" in test:
            return test


def for_gif(msg1):
    for dollar in msg1:
        if "$" in dollar:
            return dollar


def getGifUrl(search_term):
    apikey = API_KEY.Tenor_key  # test value
    lmt = 10
    ckey = "TELebot"
    # get the top 8 GIFs for the search term
    r = requests.get("https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %
                     (search_term, apikey, ckey,  lmt))
    ind = random.randint(0, 10)
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


@bot.message_handler(commands=['qrcode'])
def start_command(message):
    bot.send_message(message.chat.id, "Send me your Website URL/Text!")
    bot.register_next_step_handler(message, hello)


def hello(message):

    link = pyqrcode.create(message.text)
    link.png("code.png", scale=5)
    photo = open("code.png", "rb")
    bot.send_photo(message.chat.id, photo=photo)
    bot.send_message(message.chat.id, f"Hello {message.text}!")


@bot.message_handler(func=lambda msg1: msg1.text is not None and '$' in msg1.text)
def gifs(message):
    text = message.text.split()
    gif_text = for_gif(text)
    search_ele = gif_text[1:]
    gif = getGifUrl(search_ele)
    bot.reply_to(message, gif)


@bot.message_handler(commands=["about"])
def helping(message):
    print("into help block")
    bot.reply_to(message, "There are few commands available in this bot.\n/start - to start the bot\n/greet - to get greetings\n$(gifname) - to get gif\n@(user_name) - to get your insta profile link")


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
