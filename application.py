#Windows CMD:
#> set FLASK_APP=application
#> flask run

from flask import Flask, render_template, request, url_for
from random import randint

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", img_load=False)


    else: #POST
        while True:
            try:
                lower = request.form.get("lower")
                upper = request.form.get("upper")
                if int(lower) < 1 or int(upper) > 6:
                    error="Error: Numbers must be between 1 and 6"
                    return render_template("index.html", img_load=False, error=error)
                else:
                    number = randint(int(lower),int(upper))
                    img = str(number)+".JPG"
                    error=""
                    return render_template("index.html", number=number, img=img, lower=1, upper=1, img_load=True, error=error)
            except Exception as e:
                continue

@app.route("/page2",methods=["GET","POST"])
def page2():
    if request.method == "POST":
        #name = request.form.get("name")
        return render_template("index.html", name="Mark")

    else: #get
        return render_template("page2.html")
