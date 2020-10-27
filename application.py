#Windows CMD:
#> set FLASK_APP=application
#> flask run

#FLASK - standard
#render_template - allows us to generate HTML using Jinja2 in our templates
#request - By default, a route only answers to GET requests. You can use
###the methods argument of the route() decorator to handle different HTTP methods.
#url_for - required for gneerating URL's for static files

from flask import Flask, render_template, request, url_for
from random import randint

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def random_task():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        import json
        # # Opening JSON file
        with open('data.json') as json_file:
            data = json.load(json_file)
            n = randint(1,10)
            task = data[str(n)]
            for key, value in data.items():
                if value == task:
                    id = key
        return render_template("index.html", task=task, id=id)
    else:
        return render_template("error.html")


@app.route('/sort',methods=["GET","POST"])
def sort():
    if request.method == "GET":
        return render_template("bubble.html")
    elif request.method == "POST":
        #captures all form data 'names' as a Python dictionary
        #req = request.form
        #print(req)
        #gets the value in the form with the 'name' the_list
        _list = request.form["the_list"]
        if _list[-1] == ',':
            _list = _list[:-1]
        _list = [int(x.strip()) for x in _list.split(',')]

        n = len(_list)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if _list[j] > _list[j+1] :
                    _list[j], _list[j+1] = _list[j+1], _list[j]
        return render_template("bubble.html", _list = _list)
    else:
        return render_template("error.html")
