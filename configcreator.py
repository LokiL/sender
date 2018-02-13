import ConfigParser

config = ConfigParser.RawConfigParser()

config.add_section('Main')
config.set('Main', 'Path_To_Watching', '<Null>')
config.set('Main', 'Working_Chat_Id', '0')
config.set('Main', 'Bot_Token', '<botToken>')

with open('botconfig.cfg', 'wb') as configfile:
    config.write(configfile)