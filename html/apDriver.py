import apSTOCKS
import BC_mysqlClient
import datetime
import numpy
from scipy.signal import argrelextrema, argrelmax, argrelmin

def run_getAllTickersInRange(start, end):
    mysqlClient = BC_mysqlClient.BC_mysqlClient()
    q = "SELECT ticker, max(high) as high, min(low) as low, count(*) as c, (MAX(high) - MIN(low)) as diff FROM daily_stock WHERE time >= '" + start + "' AND time <= '" + end + "' GROUP BY ticker HAVING c >= 10 ORDER BY diff DESC LIMIT 100"
    tickers_c = mysqlClient.query(q)

    ticker_count_list = []
    for ticker_c in tickers_c:
        ticker_count_list.append({"ticker":ticker_c.get("ticker"), "c": ticker_c.get("c"), "high": ticker_c.get("high"), "low": ticker_c.get("low"), "diff":ticker_c.get("diff")})

    return ticker_count_list



def run_getAllExtrema():
    start_end = apSTOCKS.getDateRange(datetime.datetime(2017, 11, 17), 14)
    print "start range: " + str(start_end.get("start"))
    print "stop range: " + str(start_end.get("end"))

    stopwatch = apSTOCKS.BC_stopwatch()
    stopwatch.start()
    mysqlClient = BC_mysqlClient.BC_mysqlClient()
    q = "SELECT ticker, count(*) as c FROM daily_stock WHERE time >= '" + start_end.get(
        "startString") + "' AND time <= '" + start_end.get("endString") + "'  GROUP BY ticker HAVING c >= 10;"
    tickers = mysqlClient.query(q)

    count = 0
    total = tickers.__len__()

    for ticker in tickers:
        ret_range_extrema = {}
        print str(count) + " / " + str(total) + " seconds: " + str(stopwatch.elapsed())

        print ticker
        ret_range_extrema.update({"ticker": str(ticker.get("ticker")), "start": start_end.get("startString"),
                                  "end": start_end.get("endString")})
        print ret_range_extrema

        q = "SELECT close, open, high, low, time, ticker, id FROM daily_stock WHERE time >= '" + start_end.get(
            "startString") + "' AND time <= '" + start_end.get("endString") + "' AND ticker = '" + ticker.get(
            "ticker") + "' ORDER BY time;"
        stockResultSet = mysqlClient.query(q)

        print "len [" + str(stockResultSet.__len__()) + "]"

        numRows = stockResultSet.__len__()
        data_points = []
        count2 = 0
        for row in stockResultSet:
            print "\t[" + str(count2) + "] " + str(row)
            ret_range_extrema.update({"close": row.get("close"), "time": row.get("time").strftime('%Y-%m-%d')})

            data_points.append({"close": row.get("close"), "time": row.get("time").strftime('%Y-%m-%d')})

            count2 = count2 + 1

        data_poins_numpy = numpy.array(data_points)
        # print("\tdata_points: " + str(data_poins_numpy) + "  len[" + str(data_poins_numpy.size) + "]")

        tops = argrelmax(data_poins_numpy)
        topsIndexes = tops[0][:].tolist()

        valleys = argrelmin(data_poins_numpy)
        valleysIndexes = valleys[0][:].tolist()

        orderedIndexs = sorted(([0, data_points.__len__() - 1] + valleysIndexes + topsIndexes))

        print "tops" + str(topsIndexes)
        print "valleys" + str(valleysIndexes)
        print "ordered" + str(orderedIndexs)
        ret_range_extrema.update({"tops": topsIndexes, "valleys": valleysIndexes, "ordered": topsIndexes})

        extremas = []
        for x in orderedIndexs:
            extremas.append(data_poins_numpy[x])

        if extremas.__len__() > 2:
            for extrema in extremas:
                print "\t\t" + str(extrema)
                ret_range_extrema.update({"tops": topsIndexes, "valleys": valleysIndexes, "ordered": topsIndexes})

            print "\n"
        count = count + 1

    stopwatch.stop()
    print str(count) + " / " + str(total) + " seconds: " + str(stopwatch.duration)

def run_getExtrema(ticker, start, end):

    ret_range_extrema = {}
    ret_range_extrema.update({"ticker": ticker, "start": start, "end": end})

    q = "SELECT close, open, high, low, time, ticker, id FROM daily_stock WHERE time >= '" + start + "' AND time <= '" + end + "' AND ticker = '" + ticker + "' ORDER BY time;"
    mysqlClient = BC_mysqlClient.BC_mysqlClient()
    stockResultSet = mysqlClient.query(q)
    opens = []
    highs = []
    lows = []
    closes = []
    for row in stockResultSet:
        highs.append({"price": row.get("high"), "time": row.get("time").strftime('%Y-%m-%d'), "type":"high"})
        lows.append({"price": row.get("low"), "time": row.get("time").strftime('%Y-%m-%d'), "type":"low"})
        opens.append({"price": row.get("open"), "time": row.get("time").strftime('%Y-%m-%d')})
        closes.append({"price": row.get("close"), "time": row.get("time").strftime('%Y-%m-%d')})


    highs_numpy = numpy.array(highs)
    tops = argrelmax(highs_numpy)
    topsIndexes = tops[0][:].tolist()
    if highs[0].get("price") > highs[1].get("price"):
        topsIndexes.append(0)
    if highs[-1].get("price") > highs[-2].get("price"):
        topsIndexes.append(highs.__len__() - 1)


    lows_numpy = numpy.array(lows)
    valleys = argrelmin(lows_numpy)
    valleysIndexes = valleys[0][:].tolist()
    if lows[0].get("price") < lows[1].get("price"):
        valleysIndexes.append(0)
    if lows[-1].get("price")  < lows[-2].get("price"):
        valleysIndexes.append(lows.__len__() - 1)

    orderedIndexs = sorted(valleysIndexes + topsIndexes)

    ret_range_extrema.update({"tops": topsIndexes, "valleys": valleysIndexes, "ordered": orderedIndexs})

    extremas = []
    for x in orderedIndexs:
        if x in topsIndexes:
            extremas.append(highs_numpy[x])
        else:
            extremas.append(lows_numpy[x])
    if extremas.__len__() > 2:
        ret_range_extrema.update({"extremas": extremas})

    return ret_range_extrema

def getRange(ticker, start, end):
    q = "SELECT close, open, high, low, time, ticker, id FROM daily_stock WHERE time >= '" + start + "' AND time <= '" + end + "' AND ticker = '" + ticker + "' ORDER BY time;"
    mysqlClient = BC_mysqlClient.BC_mysqlClient()
    stockResultSet = mysqlClient.query(q)
    ret_range = {}
    ret_range.update({"ticker": ticker, "start": start, "end": end})
    opens = []
    highs = []
    lows = []
    closes = []
    times = []

    for row in stockResultSet:
        opens.append(row.get("open"))
        lows.append(row.get("low"))
        highs.append(row.get("high"))
        closes.append(row.get("close"))
        times.append(row.get("time").strftime('%Y-%m-%d'))

    ret_range.update({"opens": opens, "closes": closes, "highs": highs, "lows": lows, "times": times})
    return ret_range

run_getAllTickersInRange("2017-11-17", "2018-12-01")


#getRange("AABVF","2017-11-17", "2018-12-01")

#run_getExtrema("AABVF", "2017-11-17", "2017-12-01")
