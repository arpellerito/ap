#!/usr/bin/python
import apSTOCKS
import cgitb
import cgi
import BC_mysqlClient
cgitb.enable()

print "Content-Type: text/html\r\n\r\n"
form = cgi.FieldStorage()
# A nested FieldStorage instance holds the file
fileitem = form['file']

# Test if the file was uploaded


if fileitem.file:
    mysqlClient = BC_mysqlClient.BC_mysqlClient()
    # It's an uploaded file; count lines
    headerLine = fileitem.file.readline()
    headerLine = headerLine.rstrip()

    if "ticker" in headerLine:
        headerLineSplit = headerLine.split(",")
        tickerIndex = headerLineSplit.index("<ticker>")
        dateIndex = headerLineSplit.index("<date>")
        openIndex = headerLineSplit.index("<open>")
        closeIndex = headerLineSplit.index("<close>")
        highIndex = headerLineSplit.index("<high>")
        lowIndex = headerLineSplit.index("<low>")
        volIndex = headerLineSplit.index("<vol>")

        linecount = 0
        sucesscount = 0
        cont = True
        while cont:
            line = fileitem.file.readline()
            if line:
                lineSplit = line.rstrip().split(",")
                queryString = "INSERT INTO daily_stock (time, ticker, high, low, open, close, volume) values(" \
                            + lineSplit[dateIndex] + ", " \
                            + "'" + lineSplit[tickerIndex] + "', " \
                            + lineSplit[highIndex] + ", " \
                            + lineSplit[lowIndex] + ", " \
                            + lineSplit[openIndex] + ", " \
                            + lineSplit[closeIndex] + ", " \
                            + lineSplit[volIndex] \
                            + ");"
                #print queryString + "<br>"

                if mysqlClient.insert(queryString):
                    sucesscount = sucesscount + 1
                linecount = linecount + 1
                mysqlClient.commit()

            else:
                cont = False
                break

        print ("inserted [" + str(sucesscount) + " ] rows [ tried:[" + str(linecount) + "]")
else:
    print ("no file")

print "<b>done</b>"