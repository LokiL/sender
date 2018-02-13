from multiprocessing import Process, Queue

import bot, watchdog


if __name__ == '__main__':
    print('Log message: program Start')
    watchdog.watchdog()