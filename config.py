import ConfigParser
import os

config = ConfigParser.RawConfigParser()

# When adding sections or items, add them in the reverse order of
# how you want them to be displayed in the actual file.
# In addition, please note that using RawConfigParser's and the raw
# mode of ConfigParser's respective set functions, you can assign
# non-string values to keys internally, but will receive an error
# when attempting to write to a file or when you get it in non-raw
# mode. SafeConfigParser does not allow such assignments to take place.

config.add_section('sqlite')
config.set('sqlite', 'db_version', '1')
config.set('sqlite', 'db_name', 'test1.db')
config.set('sqlite', 'beer table', 'beer')
config.set('sqlite', 'coffee table', 'coffee_bean')
config.set('sqlite', 'chocolate table', 'chocolate')
config.set('sqlite', 'wine table', 'wine')
config.set('sqlite', 'spirits table', 'spirits')
config.set('sqlite', 'tea table', 'tea')

# Writing our configuration file to 'example.cfg'
with open('settings.config', 'wb') as configfile:
    config.write(configfile)
