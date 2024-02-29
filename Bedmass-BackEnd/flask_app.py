
# Continue this tutorial the next time you work on this
# https://blog.pythonanywhere.com/121/

from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return render_template("test_page.html")

