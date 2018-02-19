#!/usr/bin/python

# Turn on debug mode.
import cgitb
import cgi
import BC_htmlTemplates2

cgitb.enable()

print(BC_htmlTemplates2.header)
print(BC_htmlTemplates2.navbar)
print(BC_htmlTemplates2.progressbar)
print("""<div class="container">""")

print("""<div class="/container">""")


print (BC_htmlTemplates2.footer)
