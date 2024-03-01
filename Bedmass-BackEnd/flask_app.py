
# Continue this tutorial the next time you work on this
# https://blog.pythonanywhere.com/121/

from flask import Flask, render_template, request
from functions import addDataPatient

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return render_template("test_page.html")

@app.route('/admin')
def admin():
    return render_template("admin.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/staff')
def staff():
    return render_template("staff.html")

@app.route('/createAccount')
def create_account():
    return render_template("createAccount.html")

@app.route('/main')
def main():
    return render_template("main.html")

@app.route('/Functiontest')
def Functiontest():
    return render_template("Functiontest.html")

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = {
            'patientid': request.form['patientid'],
            'name': request.form['name'],
            'address': request.form['address'],
            'dob': request.form['dob'],
            'contact': request.form['contact']
        }
        addDataPatient("patient", data)
    except Exception as e:
        return f'Error: {str(e)}'
    