
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return render_template("test_page.html")

@app.route('/admin')
def admin():
    return render_template("admin_page.html")

@app.route('/login')
def login():
    return render_template("login_page.html")

@app.route('/staff')
def staff():
    return render_template("staff_page.html")

@app.route('/createAccount')
def create_account():
    return render_template("create_account_page.html")

@app.route('/main')
def main():
    return render_template("main_page.html")
