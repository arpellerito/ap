#!/usr/bin/python

# Turn on debug mode.
import cgitb
import apSTOCKS
from apSTOCKS import BC_InfluxDBClient
import os


import datetime

cgitb.enable()

from influxdb import InfluxDBClient


# Print necessary headers.
print("Content-Type: text/html\r\n")


# using Http
#BC_InfluxDBClient = BC_InfluxDBClient(host='127.0.0.1', port=8086, username='ap', password='ddeerr44', database='stocksDAILY')
BC_InfluxDBClient= BC_InfluxDBClient()

ticker = "TEST"
date = "1995-08-26"
high = 5
low = 4
open = 4.25
close = 4.5
volume = 999

directory = "/home/alaska/OTCBB/"
for filePath in os.listdir(directory):
    #print(directory + filePath + "</br>")
    print(BC_InfluxDBClient.insertFile(directory+filePath))

query = "select * from daily_stock where time > '2013-08-12'"

#print(BC_InfluxDBClient.insertFile(filePath))
result = BC_InfluxDBClient.InfluxDBClient.query(query)
#print("Result: {0}".format(result))
print("</br>")
print(BC_InfluxDBClient.host)
print(BC_InfluxDBClient.database)
print(datetime.datetime.now())




