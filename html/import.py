#!/usr/bin/python

# Turn on debug mode.
import cgitb
import apSTOCKS
from apSTOCKS import BC_InfluxDBClient


import datetime

cgitb.enable()

from influxdb import InfluxDBClient


# Print necessary headers.
print("Content-Type: text/html\r\n")


# using Http
BC_InfluxDBClient = BC_InfluxDBClient(host='127.0.0.1', port=8086, username='ap', password='ddeerr44', database='stocksDAILY')

ticker = "TEST"
date = "1994-08-26"
high = 5
low = 4
open = 4.25
close = 4.5
volume = 999

BC_InfluxDBClient.insert(ticker, date, high, low, open, close, volume)





print(BC_InfluxDBClient.host)
print(BC_InfluxDBClient.dbname)
print(datetime._date)




