#!/usr/bin/python

# Turn on debug mode.
import cgitb
import datetime

cgitb.enable()
# Print necessary headers.
print("Content-Type: text/html\r\n")


print("<h1>python test: </br>")
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("</h1>")

