from time import time
import telebot
import requests

API_KEY = "5729641344:AAHo-ghSD97FFEEu0W1GeWVjuWvvxRtMphw"
bot = telebot.TeleBot(API_KEY)

def splitter(msg):
    for test in msg:
        if "@" in test:
            return test

def get_img():
    content = requests.get("https://thatcopy.pw/catapi/rest/").json()
    img = content["url"]
    return img

def get_fact():
    content = requests.get("https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1").json()
    fact = content["text"]
    return fact


@bot.message_handler(commands=["start"])
def hi(message):
     bot.reply_to(message, "Welcome! \nUse /help to find How to use the Bot! \nUse /greet for greetings \nUse /meow for cat images")
    
@bot.message_handler(commands=["greet"])
def greeting(message):
    bot.send_message(message.chat.id, "hello, How are you?")

@bot.message_handler(commands=["help"])
def helping(message):
    bot.reply_to(message, "To use this, You need to verify your username")

@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
def insta_profile(message):
    texts = message.text.split()
    calling = splitter(texts)

    bot.reply_to(message, "https://instagram.com/{}".format(calling[1:]))



@bot.message_handler(commands=["meow"])
def catimg(message):
    cat = get_img()
    bot.send_photo(message.chat.id, cat) 

@bot.message_handler(commands=["catfact"])
def facts(message):
    facts = get_fact()
    bot.send_message(message.chat.id, facts)

@bot.message_handler(func=lambda m: True)
def repeat(message):
    bot.send_message(message.chat.id, message.text)

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(2)
