def greet7():
    return '''<span><!DOCTYPE html>
<html lang="en">
<head>
    <title>Green Wildflower</title>

    <!-- Recommended meta tags -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">

    <!-- PyScript CSS -->
   <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
</head>
<body>
     <button id="greet-button">Get Greeting</button>   
    <script type="py" config="./pyscript.toml" terminal>
from pyscript import when      
@when("click", "#greet-button") 
def click_handler(event):
    print("hello world")  
    display("hello")
    </script>
</body>
</html></span>'''

