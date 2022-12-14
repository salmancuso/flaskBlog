from flask import Flask, render_template

####################################################################
## Create a flask instance
####################################################################
app = Flask(__name__)


####################################################################
## Router decorators
####################################################################
@app.route('/')  #Create main index route
def index():
    return render_template("index.html")

#http://127.0.0.1:5000/user/Sal
@app.route('/user/<name>')
def user(name):
    return f"<h1>Hello {name}!!!</h1>"