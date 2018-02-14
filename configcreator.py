import ConfigParser

config = ConfigParser.RawConfigParser()

config.add_section('Main')
config.set('Main', 'Path_To_Watching', '<Null>')
config.set('Main', 'Working_Chat_Id', '0')
config.set('Main', 'Bot_Token', '<botToken>')
config.set('Main', 'Patch_To_Copy', '<Null>')
config.set('Main', 'Path_To_Outer_Usage', '<Null>')

with open('botconfig.cfg', 'wb') as configfile:
    config.write(configfile)
