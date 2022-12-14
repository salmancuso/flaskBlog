# flaskBlog
Building a simple flask blog for practice. 


## REFERENCE MATERIALS
https://www.youtube.com/playlist?list=PLCC34OHNcOtolz2Vd9ZSeSXWc8Bq23yEz


## Enviromental variables 
`export FLASK_ENV=development`
`export FLASK_APP=hello.py` -- This points to the main app. 

## Run Flask outside of python
`flask run`

## Jinja2 to pull pythonic ways into websites
https://jinja.palletsprojects.com/en/3.1.x/

## Safe in Jinja code. This will force jinja to pass HTML coming from flask. Nomrlaly html will have to be coded in the html page, but passing "Safe" you can pass HTML tags that executes
<p>{{ stuff | safe}}</p>
Other tags worth using in jinja
* trim
* safe
* capitalize
* lower
* upper
* title
* trim
* striptags

# For Loops and if statments in jinja
```
{% for topping in pizzaToppings %}
    {% if topping == 41 %}
        {{ topping + 100 }} <BR/>
    {% else % }
        {{ topping }} <BR/>
    {% endif %}
{% endfor %}

```