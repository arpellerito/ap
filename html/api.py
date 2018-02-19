#!/usr/bin/python

import cgitb
import cgi
import apSTOCKS
import BC_mysqlClient
import apDriver
import json

cgitb.enable()


form = cgi.FieldStorage()
formKeys = form.keys()

action = form.getvalue('action')

mysqlClient = BC_mysqlClient.BC_mysqlClient()

if action == 'selectCount':
    print "Content-Type: application/json\r\n\r\n"
    table = form.getvalue('table')
    print mysqlClient.count(table)
elif action == 'getRangeExtrema':
    print "Content-Type: application/json\r\n\r\n"

    start = form.getvalue('start')
    end = form.getvalue('end')
    ticker = form.getvalue('ticker')

    print json.dumps(apDriver.run_getExtrema(ticker, start, end))
elif action == 'getTickersInRange':
    print "Content-Type: application/json\r\n\r\n"

    start = form.getvalue('start')
    end = form.getvalue('end')

    print json.dumps(apDriver.run_getAllTickersInRange(start, end))
elif action == 'getRange':
    print "Content-Type: application/json\r\n\r\n"

    start = form.getvalue('start')
    end = form.getvalue('end')
    ticker = form.getvalue('ticker')

    print json.dumps(apDriver.getRange(ticker, start, end))

elif action == 'query':
    print "Content-Type: application/json\r\n\r\n"

    query = form.getvalue('query')
    resultFormat = form.getvalue('format')

    if resultFormat == 'JSON':
        #print json.dumps(mysqlClient.queryJSON(query))
        print json.dumps(mysqlClient.queryJSON(query), indent=4, sort_keys=True, default=str)

#options = {'selectCount' : BC_InfluxDBClient.count(measurement),
#           'false' : False,
#}

#//print str(options[action]());
