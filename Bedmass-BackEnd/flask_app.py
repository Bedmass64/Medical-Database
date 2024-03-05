
# Continue this tutorial the next time you work on this
# https://blog.pythonanywhere.com/121/

from flask import Flask, redirect, render_template, request, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from functions import *

app = Flask(__name__)
app.config["DEBUG"] = True

app.secret_key = 'your_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("main.html")

@app.route('/admin', methods=["GET", "POST"])
def admin():
    if request.method == 'POST':
        input_data = request.form['input_data']
        #process data (add html?)
        processed_data = readTableData(input_data)
        return render_template('admin.html', data=processed_data)
    return render_template("admin.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # This is where you would validate the username and password.
        user = User(1, 'user1', 'password') # Example user, replace with database lookup
        if username == user.username and password == user.password:
            login_user(user)
            return redirect(url_for('admin'))
    return render_template("login.html")

@app.route('/staff', methods=["GET", "POST"])
def staff():
    if request.method == 'POST':
        input_data = request.form['input_data']
        #process data (add html?)
        processed_data = readTableData(input_data)
        return render_template('staff.html', data=processed_data)

    return render_template('staff.html')

@app.route('/createAccount', methods=["GET", "POST"])
def create_account():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        email_address = request.form['email_address']
        password = request.form['password']
        speciality = request.form['speciality']
        #check if the account can be created
        #add it to the database
        #create role for the database? or do we just use one role shared for all staff
        return render_template("createAccount.html", response="Success!")
    return render_template("createAccount.html")

@app.route('/main', methods=["GET", "POST"])
def main():
    return render_template("main.html")

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

users = {1: User(1, 'user1', 'password')}

#Login Functionality
@login_manager.user_loader
def load_user(user_id):
    return users.get(int(user_id))



@app.route('/Functiontest', methods=["GET", "POST"])
def Functiontest():
    return render_template("Functiontest.html")

@app.route('/submit', methods=["GET", "POST"])
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
@app.route('/submit2', methods=["GET", "POST"])
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

@app.route('/submit3', methods=["GET", "POST"])
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

@app.route('/submit4', methods=["GET", "POST"])
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

@app.route('/submit5', methods=["GET", "POST"])
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

@app.route('/submit6', methods=["GET", "POST"])
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
