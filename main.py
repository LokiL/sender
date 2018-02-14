# -*- coding: utf-8 -*-
import ConfigParser
import telegramModule
import threading
import watchdogModule

config = ConfigParser.ConfigParser()
config.read('botconfig.cfg')

watchingPatch = config.get('Main', 'path_to_watching')

if __name__ == '__main__':
    print('Log message: program Start')

    botThread = threading.Thread(target=telegramModule.botRun)
    watchdogThread = threading.Thread(target=watchdogModule.watchdogRun, args=[watchingPatch])

    botThread.start()
    watchdogThread.start()

    botThread.join()
    watchdogThread.join()
