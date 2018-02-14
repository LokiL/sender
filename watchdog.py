import os, time, threading
import telegramModule



def watchdog(watchingPatch):
    #start botInstance in thread
    botThread = threading.Thread(target=telegramModule.botRun)
    botThread.start()

    #checking for changing
    before = dict([(f, None) for f in os.listdir(watchingPatch)])
    while 1:
        print('Log message: watchdog online')
        time.sleep(10)
        after = dict([(f, None) for f in os.listdir(watchingPatch)])
        added = [f for f in after if not f in before]
        if added:
            print("List added: ", ",".join(added))
            try:
                telegramModule.botInstance.send_message(telegramModule.current_chat_id.value, str(added))
            except Exception:
                print('Exception', Exception)
        before = after
    botThread.join()