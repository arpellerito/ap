#!/usr/bin/python

from datetime import date, datetime, timedelta
import BC_mysqlClient
import BC_InfluxDBClient


class BC_Stock:
    def __init__(self, ticker, time, high, low, open, close, volume):
        self.ticker = ticker
        self.time = time
        self.high = high
        self.low = low
        self.open = open
        self.close = close
        self.volume = volume



    def __str__(self):
        s = "ticker: " + self.ticker + " time: " + self.time + " high: " + self.high+"low"+ self.low + " open: " + self.open + " close: " + self.close + " volume: " + self.volume
        return s

class BC_range_extrema:
    def __init__(self, id, date_range, ticker, extrema):
        self.id = id
        self.date_range = date_range
        self.ticker = ticker
        self.extrema = extrema

class BC_stopwatch:
    START = None
    STOP = None
    timeDelta = None
    duration = None

    def __init__(self):
       self.status = "off"

    def start(self):
        self.START = datetime.now()
        self.status = "timing"

    def stop(self):
        self.STOP = datetime.now()
        self.timeDelta = self.STOP - self.START
        self.duration = self.timeDelta.total_seconds()
        self.status = "stopped"
        return self.duration

    def elapsed(self):
        now = datetime.now()
        timeDelta = now - self.START
        duration = timeDelta.total_seconds()
        return duration

class BC_daily_stock_list:
    def __init__(self, query=None):
        self.stock_list = []
        mysqlClient = BC_mysqlClient.BC_mysqlClient()
        if query is None:
            query = "select * from daily_stock;"
        result = mysqlClient.query(query)



class BC_range_extrema_list:
    def __init__(self, where=None):
        self.range_extrema_list = []
        mysqlClient = BC_mysqlClient.BC_mysqlClient()
        query = "SELECT * FROM range_extrema;"
        if where is not None:
            query = "SELECT * FROM range_extrema WHERE " + where + ";"

        cursor = mysqlClient.mysqlClient.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            id = row[0]
            date_range = row[1]
            ticker = row[2]
            extrema = row[3]
            range_extrema = BC_range_extrema(id, date_range, ticker, extrema)
            self.range_extrema_list.append(range_extrema)


def getDateRange(startTime=None, range=None):


    dates = []

    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    dates.append(today)

    today_plus_range = (today + timedelta(days=range))
    dates.append(today_plus_range)

    if not startTime == "today" :
        dates = []
        today = startTime
        dates.append(today)

        today_plus_range = (today + timedelta(days=range))
        dates.append(today_plus_range)

    ret_dict = {"start": min(dates), "end": max(dates), "startString": min(dates).strftime('%Y-%m-%d'), "endString": max(dates).strftime('%Y-%m-%d')}
    return ret_dict

