# -*- coding: utf-8 -*-
import os
import time

import telegramModule


class DiffCat:
    def __init__(self):
        self.addedList = None
        self.removedList = None

    def setAdded(self, added):
        self.addedList = added

    def setRemoved(self, removed):
        self.removedList = removed


changesCat = DiffCat()


def watchdogRun(watchingPatch):
    # checking for changing
    print('Log message: watchdogRun online')
    before = dict([(files, None) for files in os.listdir(watchingPatch)])
    while 1:
        time.sleep(10)
        after = dict([(files, None) for files in os.listdir(watchingPatch)])
        added = [files for files in after if not files in before]
        removed = [files for files in before if not files in after]
        if added:
            print("Log message: list added: ", ",".join(added))
            changesCat.setAdded(added)
            telegramModule.sendFileChanging(added)
        if removed:
            print("Log message: list removed: ", ",".join(removed))
            changesCat.setRemoved(removed)
        before = after
        print('Log message: watchdog cycle passed')


if __name__ == '__main__':
    watchingPath = r'D:\temp'
    watchdogRun(watchingPath)
