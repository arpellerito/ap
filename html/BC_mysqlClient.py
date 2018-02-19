#!/usr/bin/python
import MySQLdb
import csv
import os
import apSTOCKS

class BC_mysqlClient:

    def __init__(self):
        self.host = '127.0.0.1'
        self.user = 'ap'
        self.password = 'ddeerr44'
        self.database = 'apStockTrends'

        self.mysqlClient = MySQLdb.connect(host=self.host, user=self.user, passwd=self.password, db=self.database)

    def commit(self):
        self.mysqlClient.commit()

    def insert(self, query):
        cursor = self.mysqlClient.cursor()

        try:
            cursor.execute(query)
#            result = cursor.fetchall()
            for row in result:
                for item in row:
                    ret = ret + str(item) + ","
                ret = ret + '\n'
            return True
        except:
            return False

    def insert_range_extrema(self, date_range, ticker, extrema):

        query = "INSERT INTO range_extrema(date_range, ticker, extrema) values('" + date_range + "', '" + ticker + "', '" + extrema + "')"
        print query
        ret = self.query(query)
        return ret

    def insertFile(self, filePath):
        ret = False
        return ret

    def query(self, query):
        cursor = self.mysqlClient.cursor(MySQLdb.cursors.DictCursor)

        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except:
            return "false"

    def testFile(self, file):
        ret = False
        return ret

    def count(self, table):
        cursor = self.mysqlClient.cursor()
        cursor.execute("SELECT * FROM " + table + ";")
        return str(cursor.rowcount)

    def queryJSON(self, query):
        cursor = self.mysqlClient.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        ret = {}
        ret_cols = []
        for col in cursor.description:
            ret_cols.append(col)

        ret_rows = []
        for row in result:
            ret_rows.append(row)

        ret.update({'cols':ret_cols})
        ret.update({'rows':ret_rows})
        return ret