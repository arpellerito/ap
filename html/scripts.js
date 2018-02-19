$(document).ready(function(){

    $(".now").html($.now().toLocaleString());

    $("#counterButton").click(function(e){
        if($("#fileInput2Count").hasClass("active")){
            stopCount();
        }else{
            startCount();
        }
    });

    updateCount("./api.py?action=selectCount&table=daily_stock");

    $("#get_range_extrema_form").click(function(e){
        ticker = $("#range_extrema_ticker").val();
        start = $("#range_extrema_start").val();
        end = $("#range_extrema_end").val();

        json = get_range_extrema(ticker, start, end)
        $("#range_extrema_ticker_result").val("test");
    });

    $("#get_tickers_in_range_form").click(function(e){
        start = $("#get_tickers_in_range_start").val();
        end = $("#get_tickers_in_range_end").val();

        json = get_tickers_in_range(start, end)
    });

});

$(document).on('click', '.ticker_search' , function() {
        ticker = $(this).attr("ticker")
        start = $(this).attr("start")
        end = $(this).attr("end")

        get_range_extrema(ticker, start, end)

        get_plotly(ticker, start, end)
});

function startCount(){
    var url = "./api.py?action=selectCount&table=daily_stock"
    try {
        $("#fileInput2Count").addClass("active")
        $("#counterButton").text("Stop Count")
        updateCount(url)
    } catch (e) {
      console.error('update count error ', e)
    }
    return true;
}

function stopCount(){
    var url = "./api.py?action=selectCount&table=daily_stock"
    try {
      $("#fileInput2Count").removeClass("active")
      $("#counterButton").text("Start Count")
      updateCount(url)
    } catch (e) {
      console.error('update count error ', e)
    }
    return true;
}


function getJSON(url) {

    var xhr2 = new XMLHttpRequest();
    xhr2.open('GET', url, true);
    xhr2.send();
    return xhr2.response
};

function updateCount(url) {
  const xhr3 = new XMLHttpRequest();
  xhr3.timeout = 200000;
  xhr3.onreadystatechange = function(e) {
     if (xhr3.readyState === 4) {
     if (xhr3.status === 200) {
               var date = new Date()
                $(".now").text( new Date().toLocaleString());
                $("#fileInput2Count").html(xhr3.response);
                if($("#fileInput2Count").hasClass("active")
                ){
                    window.setTimeout(updateCount("./api.py?action=selectCount&table=daily_stock"), 100);
                } else {

                }

     } else {
        console.log("update count fail: " + XHR.status + " |url " + url);
     }
     }
  }
  xhr3.ontimeout = function () {
     console.log('update count : timeout')
  }

  $(".now").text( new Date().toLocaleString());
  xhr3.open('get', url, true)
  xhr3.send();
}

function get_range_extrema(ticker, start, end){
  url = "./api.py?action=getRangeExtrema&ticker=" + ticker + "&start=" + start + "&end=" + end

  XHR = new XMLHttpRequest();
  XHR.timeout = 200000;
  XHR.onreadystatechange = function(e) {
     console.log('get_range_extrema : ready state[' + XHR.readyState + "]" )

     if (XHR.readyState === 4) {
     if (XHR.status === 200) {

                $(".now").html( new Date().toLocaleString());
                json = JSON.parse(XHR.response);

                retTicker = json.ticker
                retStart = json.start
                retEnd = json.end
                retTopIndexes = "[ "+json.tops.join(', ') + " ]"
                retValleyIndexes = "[ "+json.valleys.join(', ') + " ]"
                retOrderedIndexes = "[ "+json.ordered.join(', ') + " ]"
                retExtremas = "<br>    "

                for(var extrema in json.extremas) {
                    retExtremas = retExtremas + "    " + json.extremas[extrema]["time"] + " : " + json.extremas[extrema]["price"] + "   " + json.extremas[extrema]["type"] + " <br>";
                }

                $("#range_extrema_result").html("ticker : " + retTicker + "<br>" +
                                                "start : " + retStart + "<br>" +
                                                "end : " + retEnd + "<br>" +
                                                "tops : " + retTopIndexes + "<br>" +
                                                "valleys : " + retValleyIndexes + "<br>" +
                                                "ordered : " + retOrderedIndexes + "<br>" +
                                                "extremas : " + retExtremas + "<br>"
                );

     } else {
        $("#range_extrema_result").html(XHR.status);
        console.log("get_range_extrema : " + XHR.status + " |url " + url);

     }
     }
  }
  XHR.ontimeout = function () {
     console.log('get_range_extrema : timeout')
  }

  $(".now").text( new Date().toLocaleString());
  XHR.open('get', url, true)
  XHR.send();
}

function get_tickers_in_range(start, end){
  url = "./api.py?action=getTickersInRange&&start=" + start + "&end=" + end;

  XHR = new XMLHttpRequest();
  XHR.timeout = 200000;
  XHR.onreadystatechange = function(e) {
     console.log('get_tickers_in_range : ready state[' + XHR.readyState + "]" );

     if (XHR.readyState === 4) {
     if (XHR.status === 200) {

                $(".now").html( new Date().toLocaleString());
                ticker_c_list = JSON.parse(XHR.response)
                for (var ticker_c in ticker_c_list){
                    ticker = ticker_c_list[ticker_c].ticker;
                    c = ticker_c_list[ticker_c].c;
                    high = ticker_c_list[ticker_c].high;
                    low = ticker_c_list[ticker_c].low;
                    diff = ticker_c_list[ticker_c].diff
                    li = " <li class='list-group-item d-flex justify-content-between align-items-left'> " +
                    $("#get_tickers_in_range_result_list").append("<tr><th scope='row'>" +ticker.toString() + "</th><td>" + high.toString() +"</td><td>" + low.toString() + "</td><td>" + diff.toString() + "</td><td><button type='button' class=' btn btn-primary ticker_search' ticker='" + ticker.toString()+ "' start='" + start + "' end='" + end+ "'>Plot</button></td></tr>");
                }

     } else {
        $("#tickers_in_range_result").html(XHR.status);
        console.log("tickers_in_range : " + XHR.status + " |url " + url);

     }
     }
  }
  XHR.ontimeout = function () {
     console.log('tickers_in_range : timeout')
  }

  $(".now").text( new Date().toLocaleString());
  XHR.open('get', url, true)
  XHR.send();
}

function get_plotly(ticker, start, end){

  url = "./api.py?action=getRange&ticker=" + ticker + "&start=" + start + "&end=" + end

  XHR = new XMLHttpRequest();
  XHR.timeout = 200000;
  XHR.onreadystatechange = function(e) {
     console.log('get_range : ready state[' + XHR.readyState + "]" )

     if (XHR.readyState === 4) {
     if (XHR.status === 200) {

                $(".now").html( new Date().toLocaleString());
                json = JSON.parse(XHR.response);


                var trace1 = {
                    x: json.times,
                    close: json.closes,
                    decreasing: {line: {color: '#7F7F7F'}},
                    high: json.highs,
                    increasing: {line: {color: '#17BECF'}},
                    line: {color: 'rgba(31,119,180,1)'},
                    low: json.lows,
                    open: json.opens,
                    type: 'candlestick',
                    xaxis: 'x',
                    yaxis: 'y'
                };

                var data = [trace1];

                var layout = {
                            dragmode: 'zoom',
                            margin: {
                                    r: 10,
                                    t: 10,
                                    b: 10,
                                    l: 30
                            },
                            showlegend: false,
                            xaxis: {
                                autorange: true,
                                domain: [0, 1],
                                range: [json.times[0], json.times[-1]],
                                rangeslider: {range: [json.times[0], json.times[-1]]},
                                title: 'Date',
                                type: 'date'
                            },
                            yaxis: {
                            autorange: true,
                            domain: [0, 1],
                            type: 'linear'
                            }
                     };
                Plotly.purge('plotly-div');
                Plotly.plot('plotly-div', data, layout);



     } else {

        $("#range_extrema_result").html(XHR.status);
        console.log("get_range_extrema : " + XHR.status + " |url " + url);

     }
     }
  }

  XHR.ontimeout = function () {
     console.log('get_range_extrema : timeout');
  }

  $(".now").text( new Date().toLocaleString());
  XHR.open('get', url, true);
  XHR.send();
}

