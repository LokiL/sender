import watchdogModule, ConfigParser

config = ConfigParser.ConfigParser()
config.read('botconfig.cfg')

watchingPatch = config.get('Main', 'path_to_watching')

if __name__ == '__main__':
    print('Log message: program Start')
    watchdogModule.watchdogInstance(watchingPatch)