# -*- coding: utf-8 -*-
import os

import telebot

import botToken

bot = telebot.TeleBot(botToken.token)

class chat_id:
    def __init__(self, start_state):
        self.value = 0
    def setValue(self, chat_id):
        self.value = chat_id

current_chat_id = chat_id(0)

@bot.message_handler(commands=['ping'])
def send_welcome(message):
    bot.reply_to(current_chat_id.value, "pong")

#tech chat id return
@bot.message_handler(commands=['setchatid'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Chat id сохранен')
    current_chat_id.setValue(message.chat.id)

#test sending
@bot.message_handler(commands=['testsend'])
def echo_all(message):
    bot.send_message(current_chat_id.value, "Начата загрузка файла: " + getFilePath())
    bot.send_document(current_chat_id.value, sendFile())



# tech functions
def getFilePath():
    return os.getcwd() + r'\test1.apk'


def sendFile():
    docpatch = os.getcwd() + r'\test1.apk'
    doc = open(docpatch, 'rb')
    return doc

def botRun():
    print('Log message: bot online')
    bot.polling()