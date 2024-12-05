def greet5():
    html_content = f"""
    <!DOCTYPE html>
<html lang="en">
<head>
    <title>My App</title>
    <meta charset="UTF-8">
    <iframe src="https://_12.pyscriptapps.com/matplot/latest/" height="300px" width="100%" title="Iframe Example"></iframe>

   <link rel="stylesheet" href="https://pyscript.net/releases/2023.03.1/pyscript.css" />
   <script defer src="https://pyscript.net/releases/2023.03.1/pyscript.js"></script>

</head>
<body>
    <py-script>
       import os
       print("hello")
       print(os.getcwd())
 
    </py-script>
</body>
</html>
    """
    return html_content
