from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    x = "Mark"
    return render_template("hello.html",sorted_list = x)
