#Windows CMD:
#> set FLASK_APP=application
#> flask run

#FLASK - standard
#render_template - allows us to generate HTML using Jinja2 in our templates
#request - By default, a route only answers to GET requests. You can use
###the methods argument of the route() decorator to handle different HTTP methods.
#url_for - required for gneerating URL's for static files

from flask import Flask, render_template, request, url_for, redirect
from random import randint
import os
from werkzeug.utils import secure_filename

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


def bubble(_list):
    n = len(_list)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if _list[j] > _list[j+1] :
                _list[j], _list[j+1] = _list[j+1], _list[j]
    return _list

@app.route('/sort',methods=["GET","POST"])
def sort():
    if request.method == "GET":
        return render_template("bubble.html")
    elif request.method == "POST" and "the_list" in request.form:
        #captures all form data 'names' as a Python dictionary
        #req = request.form
        #print(req)
        #gets the value in the form with the 'name' the_list
        _list = request.form["the_list"]
        #handles if there is a
        if _list:
            #splits the list of strings by comma
            _list = list(_list.split(','))
            #if multiple commas entered this removes
            #the empty list elements
            while("" in _list):
                _list.remove("")
            #this casts each element in the list to an int
            _list = [int(x) for x in _list]
            _list = bubble(_list)
        else:
            return render_template("bubble.html", _error = True)

        return render_template("bubble.html", _list = _list)
    else:
        return render_template("error.html")
#Best practice is to put this in a configuration file but for now we will just leave it here
app.config["IMAGE_UPLOADS"] = "C:/Users/mark.wood/github/randomTask/static/img/uploads"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["PNG", "JPG", "JPEG", "GIF"]
app.config["MAX_IMAGE_FILESIZE"] = 0.5 * 1024 * 1024

def allowed_image(filename):
    if not "." in filename:
        return False
    ext = filename.rsplit(".",1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False

def allowed_image_filesize(filesize):
    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False


@app.route('/upload-image',methods=["GET","POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            if not allowed_image_filesize(request.cookies.get("filesize")):
                print("File too big")
                return redirect(request.url)
            #print(request.cookies)
            #image is the 'name' of the input we used in the upload_image.html
            image = request.files["image"]
            if image.filename == "":
                print('Image must have a file name')
                return redirect(request.url)
            if not allowed_image(image.filename):
                print("That image extension is not allowed")
                return redirect(request.url)
            else:
                #sanatises the file name
                filename = secure_filename(image.filename)
                image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))

            print("image saved")
            return redirect(request.url)

    return render_template('upload_image.html')
