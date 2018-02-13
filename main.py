# -*- coding: utf-8 -*-
import telebot
import botToken #contains token = '<token_here>'
import functions

bot = telebot.TeleBot(botToken.token)

bot.polling(none_stop=False)

while True:
	pass