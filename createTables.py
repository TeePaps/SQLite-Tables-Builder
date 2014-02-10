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

con = sql.connect('test1.db')
sql.connect

with con:
    cur = con.cursor()

    ProductTable().create_table(cur)
    BeerTable(config.get('sqlite', 'beer table')).create_table(cur)
    CoffeeTable(config.get('sqlite', 'coffee table')).create_table(cur)
    ChocolateTable(config.get('sqlite', 'chocolate table')).create_table(cur)
    WineTable(config.get('sqlite', 'wine table')).create_table(cur)
    SpiritsTable(config.get('sqlite', 'spirits table')).create_table(cur)
    TeaTable(config.get('sqlite', 'tea table')).create_table(cur)

    cur.execute("INSERT INTO products(product) VALUES ('cat');")
    con.commit()

