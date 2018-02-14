# -*- coding: utf-8 -*-
import ConfigParser
import os
from shutil import copy2

import telebot

config = ConfigParser.ConfigParser()
config.read('botconfig.cfg')
botToken = config.get('Main', 'bot_token')
watchingPatch = config.get('Main', 'path_to_watching')
copyPath = config.get('Main', 'path_to_copy')
outerPath = config.get('Main', 'path_to_outer_usage')

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


# def sendLastFile(filePath):
#     if checkChatId(False) == 0:
#         print("Log message: I'm sorry Dave. I'm afraid I can't do that. Chat Id not set.")
#     else:
#         botInstance.send_message(currentChatId.value, "Начата загрузка файла: " + filePath)
#         botInstance.send_document(currentChatId.value, getFileToSend(filePath))


def sendFileChanging(filename):
    if checkChatId(False) == 0:
        print("Log message: I'm sorry Dave. I'm afraid I can't do that. Chat Id not set.")
    else:
        print("Log message: filesize more than 50mb, upload to server started")
        try:
            copy2(watchingPatch + filename[0], copyPath)
            print("Log message: filesize more than 50mb, upload to server " + copyPath + " completed")
            botInstance.send_message(currentChatId.value, "Размер файла "
                                     + filename[0] +
                                     " не позволяет загрузить его через Telegram. Ссылка на файл: "
                                     + outerPath + filename[0])
        except:
            botInstance.send_message(currentChatId.value, "I'm sorry Dave. I'm afraid I can't do that.")
        # if checkFileSize(os.stat(watchingPatch + filename[0]).st_size) == True:
        #     print("Log message: filesize less than 50mb, upload started")
        #     botInstance.send_message(currentChatId.value,
        #                              "Размер файла позволяет загрузить его через Telegram. Начата загрузка: " +
        #                              filename[0])
        #     botInstance.send_document(currentChatId.value, getFileToSend(filename))
        # else:
        #     print("Log message: filesize more than 50mb, upload to server started")
        #     copy2(watchingPatch + filename[0], copyPath)
        #     botInstance.send_message(currentChatId.value,
        #                              "Размер файла " + filename[0] +
        #                              "не позволяет загрузить его через Telegram. Ссылка на файл: "
        #                              + copyPath + filename[0])


def botRun():
    print('Log message: botInstance online')
    botInstance.polling()


def getFileToSend(filename):
    docpatch = watchingPatch + filename[0]
    doc = open(docpatch, 'rb')
    return doc


def checkFileSize(filesize):
    if filesize / 1024 <= 51200:
        a = True
    else:
        a = False
    return a


if __name__ == '__main__':
    botInstance.polling()
