# -*- coding: utf-8 -*-
import telebot
import botToken
from os import getcwd

bot = telebot.TeleBot(botToken.token)

@bot.message_handler(commands=['ping'])
def send_welcome(message):
	bot.reply_to(message, "pong")


@bot.message_handler(commands=['getchatid'])
def send_welcome(message):
    bot.send_message(message.chat.id, str(message.chat.id))

@bot.message_handler(commands=['testsend'])
def echo_all(message):
    bot.send_message(message.chat.id, "Начата загрузка файла: "+getFilePath())
    bot.send_document(message.chat.id, sendFile())

def getFilePath():
    return getcwd() + r'\test1.apk'

def sendFile():
    docpatch = getcwd() + r'\test1.apk'
    doc = open(docpatch, 'rb')
    return doc



bot.polling()

while True:
	pass