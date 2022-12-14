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
    first_name = "John"
    stuff = "this is <strong>bold</strong> text"
    pizzaToppings = ["Cheese", "Sauce", "Mushrooms", "Olivs", "Sausage", 41]
    return render_template("index.html", firstName = first_name, stuff=stuff, pizzaToppings=pizzaToppings )

#http://127.0.0.1:5000/user/Sal
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", userName=name)


####################################################################
## Error Handeling
####################################################################
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internalServerError(e):
    return render_template("500.html"), 500
