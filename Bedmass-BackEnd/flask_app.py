
# Continue this tutorial the next time you work on this
# https://blog.pythonanywhere.com/121/

from flask import Flask, render_template, request
from functions import *

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
    
#These all have temp route names and will be changed later
@app.route('/submit2', methods=['POST'])
def submit2():
    try:
        data = {
            'appointmentid': request.form['appointmentid'],
            'doctorid': request.form['doctorid'],
            'patientid': request.form['patientid'],
            'date': request.form['date'],
            'time': request.form['time'],
            'purpose': request.form['purpose']
        }
        addDataAppointment("appointment", data)
    except Exception as e:
        return f'Error: {str(e)}'
    
@app.route('/submit3', methods=['POST'])
def submit3():
    try:
        data = {
            'billid': request.form['billid'],
            'patientid': request.form['patientid'],
            'date': request.form['date'],
            'amount': request.form['amount'],
            'paymethod': request.form['paymethod'],
            'appointmentid': request.form['appointmentid']
        }
        addDataBilling("billing", data)
    except Exception as e:
        return f'Error: {str(e)}'

@app.route('/submit4', methods=['POST'])
def submit4():
    try:
        data = {
            'doctorid': request.form['doctorid'],
            'name': request.form['name'],
            'specialize': request.form['specialize'],
            'contact': request.form['contact'],
            'role': request.form['role']
        }
        addDataDoctor("doctor", data)
    except Exception as e:
        return f'Error: {str(e)}'

@app.route('/submit5', methods=['POST'])
def submit5():
    try:
        data = {
            'historyid': request.form['historyid'],
            'patientid': request.form['patientid'],
            'diagnosis': request.form['diagnosis'],
            'treatment': request.form['treatment'],
            'date': request.form['date']
        }
        addDataMedicalHistory("medical_history", data)
    except Exception as e:
        return f'Error: {str(e)}'

@app.route('/submit6', methods=['POST'])
def submit6():
    try:
        data = {
            'adminid': request.form['adminid'],
            'name': request.form['name'],
            'role': request.form['role'],
            'contact': request.form['contact']
        }
        addDataAdmin("admin", data)
    except Exception as e:
        return f'Error: {str(e)}'
