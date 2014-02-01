"""
FILE:         table.py
AUTHOR:       Ted Papaioannou
DATE BEGAN:   01/31/2014

DESCRIPTION:  This class is to create a table
"""

import sqlite3 as sql
import abc

class Table(object):

    def __init__(self, tableName):
        self.tableName = tableName
        self.tableDef = ''
        self.columns = {}

    def create_table(self, cursor):
        cursor.execute('DROP TABLE IF EXISTS %s' % self.tableName)
        cursor.execute('CREATE TABLE %s(%s)' % (self.tableName, self.tableDef))

    def set_cols(self, columns):
        """Overwrite the existing columns
        columns - a dict:
            key:    column name
            value:  column definition
        """
        self.columns = columns

    def add_cols(self, columns):
        """Append the current columns
        columns - a dict:
            key:    column name
            value:  column definition
        """
        self.columns = dict(self.columns.items() + columns.items())

    def build_table_def(self):
        """Builds the (key value, key value) string to define the table

        Source: http://codereview.stackexchange.com/questions/7953/ \
                how-do-i-flatten-a-dictionary-into-a-string
        """
        self.tableDef = (', '.join("%s %s" % (key,val.strip("'")) \
            for (key,val) in self.columns.iteritems()))
        print self.tableDef

class ProductTable(Table):
    def __init__(self):
        super(ProductTable, self).__init__('products')
        super(ProductTable, self).add_cols(dict([ \
                ('_id', 'INT PRIMARY KEY'), \
                ('product', 'TEXT'), \
                ('producer', 'TEXT'), \
                ('product_class', 'TEXT'), \
                ('product_group', 'TEXT') \
                ]))
        super(ProductTable, self.build_table_def())

class MetaTable(Table):

    def __init__(self, table_name):
        super(MetaTable, self).__init__(table_name)
        super(MetaTable, self).set_cols(dict([('product_id', \
                'INT REFERENCES Products(_id)')]))

class BeerTable(MetaTable):

    def __init__(self):
        super(BeerTable, self).__init__('beer')
        super(BeerTable, self).add_cols(dict([ \
                ('abv', 'INT') \
                ]))
        super(BeerTable, self.build_table_def())

class CoffeeTable(MetaTable):

    def __init__(self):
        super(CoffeeTable, self).__init__('coffee_bean')
        super(CoffeeTable, self).add_cols(dict([ \
                ('country', 'TEXT') \
                ]))
        super(CoffeeTable, self.build_table_def())

class ChocolateTable(MetaTable):
    def __init__(self):
        super(ChocolateTable, self).__init__('chocolate')
        super(ChocolateTable, self).add_cols(dict([ \
                ('cacoa', 'INT') \
                ]))
        super(ChocolateTable, self.build_table_def())

class WineTable(MetaTable):
    def __init__(self):
        super(WineTable, self).__init__('wine')
        super(WineTable, self).add_cols(dict([ \
                ('vintage', 'INT') \
                ]))
        super(WineTable, self.build_table_def())

class SpiritsTable(MetaTable):
    def __init__(self):
        super(SpiritsTable, self).__init__('spirits')
        super(SpiritsTable, self).add_cols(dict([ \
                ('age', 'INT') \
                ]))
        super(SpiritsTable, self.build_table_def())

class TeaTable(MetaTable):
    def __init__(self):
        super(TeaTable, self).__init__('tea')
        super(TeaTable, self).add_cols(dict([ \
                ('age', 'INT') \
                ]))
        super(TeaTable, self.build_table_def())


