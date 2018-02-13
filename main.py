# -*- coding: utf-8 -*-
import telebot
import botToken

bot = telebot.TeleBot(botToken.token)

@bot.message_handler(commands=['ping'])
def send_welcome(message):
	bot.reply_to(message, "pong")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()

while True:
	pass