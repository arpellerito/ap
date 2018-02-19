#!/usr/bin/python

# Turn on debug mode.
import cgitb
import cgi
import BC_htmlTemplates2
import datetime


cgitb.enable()

print(BC_htmlTemplates2.header)
print(BC_htmlTemplates2.navbar)
print(BC_htmlTemplates2.progressbar)
print("""<div class="container">""")
print("""<div class="card border-primary mb-3 ap-mainElement " >
            <h4><div class="card-header">Daily Stock</div></h4>
            <ul class="list-group">

                <li class="list-group-item d-flex justify-content-between align-items-center">
                    <span>Records: <b><span class="" id="fileInput2Count"></span></b></span>
                </li>
                <li class="list-group-item d-flex justify-content-between align-items-center">
                    <span>Time: <b><span class="now"><script>new Date().toLocaleString()</script></span></b></span>
                </li>
                <li class="list-group-item d-flex justify-content-between align-items-center">
                    <button type="button" class="btn btn-outline-danger" id="counterButton">Start Count</button>
                </li>
            </ul> 

        </div>""")

print(BC_htmlTemplates2.fileInput2)
print("""<div class="card border-primary mb-3 ap-mainElement" id="fileInput2Result""> File Input2 Result</div>""")



print("""<div class="/container">""")


print (BC_htmlTemplates2.footer)
