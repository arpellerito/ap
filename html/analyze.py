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

print("""
   <div class="card border-primary mb-3 ap-mainElement " >

   <ul class="list-group">

                <li class="list-group-item d-flex justify-content-between align-items-center">
                    <div class="now"></div>
                </li>
    </ul> 
   </div>
""")

print("""
   <div class="card border-primary mb-3 ap-mainElement " >
   <ul class="list-group">
                <li class="list-group-item d-flex justify-content-between align-items-center">
                    <div><input type="button" id="get_tickers_in_range_form" value="Search" class="btn btn-primary"/></div>
                </li>
                <li class="list-group-item d-flex justify-content-between align-items-center">
                    start:
                    <br><div><input type="text"  id="get_tickers_in_range_start" name="start" /></div>
                </li>
                <li class="list-group-item d-flex justify-content-between align-items-center">
                    <div>end : </div> 
                    <br>
                    <div><input type="text"  id="get_tickers_in_range_end" name="end" /></div>
                </li>                 
   </div>
""")

print("""
   <div class="card border-primary mb-3 ap-mainElement " >

   <ul class="list-group scroll-500px" id="">

                <li class="list-group-item d-flex justify-content-between align-items-center">
                <table class='table table-fixed'>
                   <thead>
                        <tr>
                            <th scope="col">ticker</th>
                            <th scope="col">high</th>
                            <th scope="col">low</th>
                            <th scope="col">diff</th>

                            <th scope="col">plot</th>
                        </tr>
                    </thead >

                    <tbody id="get_tickers_in_range_result_list">



                    </tbody>

                </table> 
                </li>
    </ul> 
   </div>
""")

print("""
   <div class="card border-primary mb-3 ap-mainElement " >
        <h4><div class="card-header">TICK</div></h4>
        <div id="plotly-div"class="">
        </div>               
    </ul> 
   </div>
""")


print ("""
   <div class="card border-primary mb-3 ap-mainElement " >
   <h4><div class="card-header">Search Ticker</div></h4>
   <ul class="list-group">

                <li class="list-group-item d-flex justify-content-between align-items-center">
                    ticker : 
                    </br>
                    <div><input type="text"  id="range_extrema_ticker" name="ticker" /></div>
                </li>
                <li class="list-group-item d-flex justify-content-between align-items-center">
                    start : 
                    </br><div><input type="text"  id="range_extrema_start" name="start" /></div>
                </li>
                <li class="list-group-item d-flex justify-content-between align-items-center">
                    end : 
                    </br>
                    <div><input type="text"  id="range_extrema_end" name="end" /></div>
                </li>
                <li class="list-group-item d-flex justify-content-between align-items-center">
                    <div><input type="button" id="get_range_extrema_form" value="Search" class="btn btn-primary"/></div>
                </li>

    </ul> 
   </div>
""")


print("""
   <div class="card border-primary mb-3 ap-mainElement " >

   <ul class="list-group .scroll-10em">

                <li class="list-group-item d-flex justify-content-between align-items-center ">
                    <div id="range_extrema_result">range_extrema_result</div>
                </li>
    </ul> 
   </div>
""")


print (BC_htmlTemplates2.footer)
