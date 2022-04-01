# include Flask class from file flask
# include Flask class from file flask
from flask import Flask

 
# create an instance of Flask class
# __name__ is a predefined setup variable
myapp_obj = Flask(__name__)
 
# different URL the app will implement

@myapp_obj.route("/")
# called view function
def hello():
    name = {'username': 'Lisa'}
    return f'''
    <html>
    <head>
    <title>Home Page - my blog</title>
    </head>
    <body>
        <h1> Welcome { name["username"]}</h1>
        <p><a href="https://www.google.com">not google</a></p>

<ul>
  <li>Paris</li>
  <li>London</li>
  <li>Rome</li>
  <li>Tahiti</li>
</ul>  

    </body>
    '''

myapp_obj.run(debug=True)

        

