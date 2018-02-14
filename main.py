import watchdogModule, ConfigParser, threading
import telegramModule
import Queue

config = ConfigParser.ConfigParser()
config.read('botconfig.cfg')

watchingPatch = config.get('Main', 'path_to_watching')

if __name__ == '__main__':
    print('Log message: program Start')
    # start instances in thread
    qe = Queue.Queue()

    botThread = threading.Thread(target=telegramModule.botRun)
    watchdogThread = threading.Thread(target=watchdogModule.watchdogRun, args=[watchingPatch])

    botThread.start()
    watchdogThread.start()

    botThread.join()
    watchdogThread.join()