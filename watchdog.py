import os, time, threading
import bot


watching_patch = r"d:\temp\111"

def watchdog():
    #start bot in thread
    botThread = threading.Thread(target=bot.botRun)
    botThread.start()

    #checking for changing
    before = dict([(f, None) for f in os.listdir(watching_patch)])
    while 1:
        print('Log message: watchdog online')
        time.sleep(10)
        after = dict([(f, None) for f in os.listdir(watching_patch)])
        added = [f for f in after if not f in before]
        if added:
            print("List added: ", ",".join(added))
            try:
                bot.bot.send_message(bot.current_chat_id.value, str(added))
            except Exception:
                print('Exception', Exception)
        before = after
    botThread.join()