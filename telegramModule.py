# -*- coding: utf-8 -*-
import os, telebot, ConfigParser

config = ConfigParser.ConfigParser()
config.read('botconfig.cfg')
botToken = config.get('Main', 'bot_token')

botInstance = telebot.TeleBot(botToken)

class chat_id:
    def __init__(self, start_state):
        self.value = 0
    def setValue(self, chat_id):
        self.value = chat_id

current_chat_id = chat_id(0)

#tech chat id return
@botInstance.message_handler(commands=['setchatid'])
def send_welcome(message):
    botInstance.send_message(message.chat.id, 'Chat id сохранен')
    print('Log message: program Start')
    current_chat_id.setValue(message.chat.id)

#test sending
@botInstance.message_handler(commands=['testsend'])
def echo_all(message):
    botInstance.send_message(current_chat_id.value, "Начата загрузка файла: " + getFilePath())
    botInstance.send_document(current_chat_id.value, getFileToSend())

# tech functions
def getFilePath():
    return os.getcwd() + r'\test1.apk'

def getFileToSend():
    docpatch = os.getcwd() + r'\test1.apk'
    doc = open(docpatch, 'rb')
    return doc

def botRun():
    print('Log message: botInstance online')
    botInstance.polling()