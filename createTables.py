"""
FILE:         createTables.py
AUTHOR:       Ted Papaioannou
DATE BEGAN:   01/31/2014

DESCRIPTION:  This will be used to create all the tables used in the
              Gastrograph Reviews AutoCompleteTextView for products
              of all classes and groups.
"""

import sqlite3 as sql
import ConfigParser
from table import *

config = ConfigParser.RawConfigParser()
config.read('settings.config')

DB_VERSION = config.get('sqlite', 'db_version')
DB_NAME = config.get('sqlite', 'db_name')
DB_TABLES = config.get('sqlite', 'tables')

con = sql.connect('test1.db')
sql.connect

with con:
    cur = con.cursor()

    ProductTable().create_table(cur)
    BeerTable().create_table(cur)
    CoffeeTable().create_table(cur)
    ChocolateTable().create_table(cur)
    WineTable().create_table(cur)
    SpiritsTable().create_table(cur)
    TeaTable().create_table(cur)

    con.commit()

