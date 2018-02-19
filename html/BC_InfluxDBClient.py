#!/usr/bin/python
from influxdb import InfluxDBClient
import csv
import os
import apSTOCKS

class BC_InfluxDBClient:

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = '8086'
        self.user = 'ap'
        self.password = 'ddeerr44'
        self.database = 'stocksDAILY'

        self.measurement = ""
        self.tags = {}
        self.time = ""
        self.fields = {}
        self.json_body = [

        ]
        self.InfluxDBClient = InfluxDBClient(self.host, self.port, self.user, self.password, self.database)

    def insert(self, ticker, date, high, low, Open, close, volume):
        ret = ""
        json_body = [
            {
                "measurement": "daily_stock",
                "tags": {
                    "ticker": ticker,
                    "high": high,
                    "low": low,
                    "open": Open,
                    "close": close,

                },
                "time": date,
                "fields": {
                    "volume": volume,

                    }
            }
        ]
        return self.InfluxDBClient.write_points(json_body)

    def insertFile(self, filePath):
        ret = ""
        dateStr = os.path.splitext(filePath)[0].split("_")[1]
        yyyy = dateStr[:4]
        mm = dateStr[4:6]
        dd = dateStr[6:]
        Date = ret + yyyy + "-" + mm + "-" + dd

        ret = "<h2>Inserting File: " + filePath + " date: " + Date + "<h2></br></br>"
        linesCount = 0
        successfulAdds = 0
        with open(filePath, "r") as importFile:
            stopwatch = apSTOCKS.BC_stopwatch()
            stopwatch.start()
            csvReader = csv.DictReader(importFile)
            for row in csvReader:
                linesCount = linesCount + 1
                Ticker = row['<ticker>']
                High = row['<high>']
                Low = row['<low>']
                Open = row['<open>']
                Close = row['<close>']
                Volume = row['<vol>']

                if self.insert(Ticker, Date, High, Low, Open, Close, Volume):
                    successfulAdds = successfulAdds + 1
        stopwatch.stop()
        ret = ret + "<b>Duration: " + str(stopwatch.timeDelta) + "secs</b></br>"
        ret = ret + "<b>lines: " + str(linesCount) + "         successful adds: " + str(successfulAdds) + "</b></br></br>"
        return ret

    def query(self, query):
        result = self.InfluxDBClient.query(query)
        points = result.get_points()

        ret = []
        for point in points:
            ret.append(str(point))
        return "\n".join(ret)

    def testFile(self, file):
        ret = ""
        return ret

    def count(self, measurement):
        query = "SELECT count(volume) FROM " + "daily_stock" + ";"
        json = self.InfluxDBClient.query(query)
        count = str(json)
        return json