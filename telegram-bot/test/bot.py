
import os
import telebot
import pickle
import json

from ip import get_ip

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg = "Heyy, How you doin?? Let me help you through this\ntype command /help for more info"
    bot.reply_to(message, msg)

@bot.message_handler(commands=['help'])
def help(message):
    msg = "/ip : Get your ip address and more info about location\n/help : Get this info"
    bot.reply_to(message, msg)

@bot.message_handler(commands=['ip'])
def my_ip(message):
    data = get_ip()

    ip = data['ip']
    city = data['city']
    region = data['region']
    loc = data['loc']
    postal = data['postal']

    bot.reply_to(message,f"Ip : {ip}\nCity : {city}\nRegion : {region}\nLOC : {loc}\nPostal : {postal}\n")


bot.infinity_polling()