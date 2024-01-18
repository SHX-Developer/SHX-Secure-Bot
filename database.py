import telebot
import sqlite3
import datetime

import config





#  LIBRARY VARIABLES

bot = telebot.TeleBot(config.token)

db = sqlite3.connect("bot.db", check_same_thread=False)
sql = db.cursor()

date_time = datetime.datetime.now().date()





#  DATABASE

def database():
    pass
