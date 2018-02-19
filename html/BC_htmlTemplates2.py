header = """Content-Type: text/html\r\n
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Import</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="bootstrap2.css">
  <link href="https://use.fontawesome.com/releases/v5.0.4/css/all.css" rel="stylesheet">
  <link rel="stylesheet" href="navbar.css">
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/js/bootstrap.min.js" integrity="sha384-a5N7Y/aK3qNeh15eJKGWxsqtnX/wWdSZSKp+81YjTmS15nvnvxKHuzaWwXHDli+4" crossorigin="anonymous"></script>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script src="scripts.js"></script>

</head>
<body>
"""

navbar = """
<nav class="navbar  navbar-expand-md navbar-dark bg-primary ">
    
    <a class="navbar-brand" href="#">Navbar</a>
    
    
    <div class="float-xs-left">
        <a class="navItem" href="./home.py">
            <i class="fas fa-user"></i>    
        </a>
    </div>
    <div class="float-xs-left">
        <a class="navItemActive" href="./home.py">
            Home   
        </a>
    </div>
        <div class="float-xs-left">
        <a class="navItem " href="./analyze.py">
            Analyze   
        </a>
    </div>
    </div>
    <div class="float-xs-left">
        <a class="navItem " href="./home.py">
            Import   
        </a>
    </div>
  
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>


    <div class="collapse navbar-collapse  justify-content-end" id="navbarSupportedContent">

        <form class="form-inline ">
            <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
  </div>
</nav>

</nav>

"""



navbar2 = """

<nav class="navbar navbar-expand-sm navbar-dark bg-primary">
    <a class="navbar-brand" href="./home.py">apStocks</a>
    
    <a class="" href="./home.py">
        <i class="fas fa-user"></i>    
    </a>
    <a class="" href="./home.py">
        <i class="fas fa-cogs"></i>    
    </a>

</nav>

"""

loadbars = """
<div class="progress ">
  <div class="progress-bar bg-success" role="progressbar" style="width: 45%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<div class="progress">
  <div class="progress-bar bg-info" role="progressbar" style="width: 50%" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<div class="progress">
  <div class="progress-bar bg-warning" role="progressbar" style="width: 55%" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<div class="progress">
  <div class="progress-bar bg-danger" role="progressbar" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
</div>
"""

fileInput = """

<form class="card border-primary mb-3 ap-mainElement" id="fileInputForm" method="post" enctype="multipart/form-data">

  <fieldset>
    <legend>Legend</legend>
    <div class="form-group">
      <label for="exampleInputFile">File input</label>
      <input class="form-control-file" id="InputFile" type="file">
    </div>
    <button onclick="" type="submit" class="btn btn-primary">Submit</button>
  </fieldset>
</form>

"""
fileInput2 = """
   <div class="card border-primary mb-3 ap-mainElement " >
   <h4><div class="card-header">File Import</div></h4>
   <form class="" enctype="multipart/form-data" action="#" method="post" id="fileForm">
    <ul class="list-group">

                <li class="list-group-item d-flex justify-content-between align-items-center">
                    <div><input type="file"  id="file" name="file" /></div>
                </li>
                <li class="list-group-item d-flex justify-content-between align-items-center">
                    <div><input type="submit" value="Upload" class="btn btn-primary"/></div>
                </li>
                
    </ul> 
   </form>
   </div>


"""

progressbar = """

<div class="progress topProgress" style="width: 100%; display: none;">
  <div class="progress-bar bg-danger topProgress" role="progressbar" style="width: 100%; display: none;" aria-valuenow="1" aria-valuemin="0" aria-valuemax="100"></div>
</div>

"""

footer = """

</body>
</html>

"""


def writeHeader():
    ret = "Content-Type: text/html\r\n"
    ret += ""




