
import os
import telebot
from ip import get_ip

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    msg = "Heyy, How you doin?? Let me help you through this type command /help for more info"
    bot.reply_to(message, msg)

@bot.message_handler(commands=['ip'])
def my_ip(message):
    data = get_ip()

    ip = data['ip']
    city = data['city']
    region = data['region']
    loc = data['loc']
    postal = data['postal']

    bot.reply_to(message,f"ip : {ip}, city : {city}, region : {region}, loc : {loc}, postal : {postal}")


bot.infinity_polling()