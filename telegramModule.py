# -*- coding: utf-8 -*-
import os, telebot, ConfigParser

config = ConfigParser.ConfigParser()
config.read('botconfig.cfg')
botToken = config.get('Main', 'bot_token')
watchingPatch = config.get('Main', 'path_to_watching')

botInstance = telebot.TeleBot(botToken)

class ChatId:
    def __init__(self):
        self.value = 0
    def setValue(self, chat_id):
        self.value = chat_id

currentChatId = ChatId()
currentChatId.value = config.get('Main', 'Working_Chat_Id')

def checkChatId(info):
    if currentChatId.value == 0:
        if info:
            print("Warning, chat id not set!")
        return 0
    else:
        if info:
            print("Log message: current chat id is " + str(currentChatId.value))
        return 1

@botInstance.message_handler(commands=['setchatid'])
def setupChatId(message):
    currentChatId.setValue(message.chat.id)
    config.set('Main', 'Working_Chat_Id', currentChatId.value)
    with open('botconfig.cfg', 'wb') as configfile:
        config.write(configfile)
    botInstance.send_message(currentChatId.value, 'Chat id сохранен')
    print('Log message: chat id: ' + str(message.chat.id) + ' saved')

def sendLastFile(filePath):
    if checkChatId(False) == 0:
        print("Log message: I'm sorry Dave. I'm afraid I can't do that. Chat Id not set.")
    else:
        botInstance.send_message(currentChatId.value, "Начата загрузка файла: " + filePath)
        botInstance.send_document(currentChatId.value, getFileToSend())

def sendFileChanging(filename):
    if checkChatId(False) == 0:
        print("Log message: I'm sorry Dave. I'm afraid I can't do that. Chat Id not set.")
    else:
        botInstance.send_message(currentChatId.value, "Начата загрузка файла: " + filename[0])
        try:
            botInstance.send_document(currentChatId.value, getFileToSend(filename))
        except:
            botInstance.send_message(currentChatId.value, "Log message: something went wrong - ", Exception)

        # botInstance.send_message(currentChatId.value, "Изменения " + str(files))
        # print("Log message: changes sended")

# #test sending
# @botInstance.message_handler(commands=['testsend'])
# def echo_all(message):
#     botInstance.send_message(currentChatId.value, "Начата загрузка файла: " + getFilePath())
#     botInstance.send_document(currentChatId.value, getFileToSend())

# # tech functions
# def getFilePath():
#     return os.getcwd() + r'\test1.apk'
#
def botRun():
    print('Log message: botInstance online')
    botInstance.polling()


def getFileToSend(filename):
    docpatch = watchingPatch+filename[0]
    doc = open(docpatch, 'rb')
    return doc



if __name__ == '__main__':
    botInstance.polling()