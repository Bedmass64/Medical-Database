from flask import Flask, redirect, url_for, request, render_template
from functions import *

app = Flask(__name__)
app.config["DEBUG"] = True

#If we are using supabase, Riley may edit this and login/ create account fields
from supabase import create_client, Client

url: str = "https://rdiogfocbfebfkvoyvoj.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJkaW9nZm9jYmZlYmZrdm95dm9qIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDgwMDUyMTIsImV4cCI6MjAyMzU4MTIxMn0.WX0hS7III4FjNkIvaPCpN0zovU88i2UaRdCdHBr-P8o"

supabase: Client = create_client(url, key)

#Main Page--------------------------------------------------------

#Mostly used for GET, simply brings them to the main page
@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("main.html")

#Mostly used for GET, simply brings them to the main page
@app.route('/main', methods=["GET", "POST"])
def main():
    return render_template("main.html")


#Login Page-------------------------------------------------------

#Login, if the method is POST, the patient is trying to login. They will send fields:
#request.json.username, request.json.password, request.json.role
#If success, login and redirect to main, else redirect to login
#If the method is GET, redirect to login page
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        #request.json.username, request.json.password, request.json.role are the fields
        #We must log in and redirect based on these fields

        username = request.form['username']
        password = request.form['password']
        # This is where you would validate the username and password.
        user = User(1, 'user1', 'password') # Example user, replace with database lookup
        if username == user.username and password == user.password:
            login_user(user)
            return redirect(url_for('adminPatients'))
    else:
        return render_template("login.html")


#Logout user and rediret to main page
@app.route('/logout', methods=['POST'])
def logout():
    user = supabase.auth.logout() #logout logic
    return redirect(url_for('main'))


#Create Account-----------------------------------------------------

#For POST, login with fields stated below. If success, log user in and create an account and
#redirect to main page. If not, throw an error
#For GET, render the create html page
@app.route('/createAccount', methods=["GET", "POST"])
def create_account():
    if request.method == 'POST':
        first_name = request.json.firstname
        last_name = request.json.lastname
        phone_number = request.json.number
        email_address = request.json.email
        password = request.json.password
        speciality = request.json.specialty
        #check if the account can be created
        #add it to the database
        #create role for the database? or do we just use one role shared for all staff
        return render_template("main")
    return render_template("create.html")

#Admin Pages---------------------------------------------------------

#If POST, return JSON data of the patients corresponding the the last name sent with
#response.json.name
#if GET, render template to corresponding html file
@app.route('/adminPatients', methods=["GET", "POST"])
def admin_patients():
    if request.method == 'POST':
        #search supabase for data and return, using request data
        return render_template('adminPatients.html')

    else:
        return render_template('adminPatients.html')

#If POST, return JSON data of the billing corresponding the patientid sent with
#response.json.patientid
#if GET, render template to corresponding html file
@app.route('/adminBilling', methods=["GET", "POST"])
def admin_billing():
    if request.method == 'POST':
        #search supabase for data and return, using request data
        render_template('adminBilling.html')
    else:
        return render_template('adminBilling.html')

#If POST, return JSON data of the records corresponding the patientid sent with
#response.json.patientid
#if GET, render template to corresponding html file
@app.route('/adminRecords', methods=["GET", "POST"])
def admin_records():
    if request.method == 'POST':
        #search supabase for data and return, using request data
        render_template('adminRecords.html')

    else:
        return render_template('adminRecords.html')

#If POST, return JSON data of the appointemnts corresponding the date sent with
#response.json.date in (YYYY-MM-DD) format
#if GET, render template to corresponding html file
@app.route('/adminAppointments', methods=["GET", "POST"])
def admin_appointments():
    if request.method == 'POST':
        #search supabase for data and return, using request data
        #Search by DATE
        return render_template('adminAppointments.html')

    else:
        return render_template('adminAppointments.html')

#Staff Pages--------------------------------------------------------

#If POST, return JSON data of the patients corresponding the the last name sent with
#response.json.name
#if GET, render template to corresponding html file
@app.route('/staffPatients', methods=["GET", "POST"])
def staff_patients():
    if request.method == 'POST':
        #search supabase for data and return, using request data
        return render_template('staffPatients.html')

    else:
        return render_template('staffPatients.html')

#If POST, return JSON data of the appointemnts corresponding the date sent with
#response.json.date in (YYYY-MM-DD) format
#if GET, render template to corresponding html file
@app.route('/staffAppointments', methods=["GET", "POST"])
def staff_appointments():
    if request.method == 'POST':
        #search supabase for data and return, using request data
        #Search by DATE
        return render_template('staffAppointments.html')+

    else:
        return render_template('staffAppointments.html')


#If POST, return JSON data of the records corresponding the patientid sent with
#response.json.patientid
#if GET, render template to corresponding html file
@app.route('/staffRecords', methods=["GET", "POST"])
def staff_records():
    if request.method == 'POST':
        #search supabase for data and return, using request data
        return render_template('staffRecords.html')

    else:
        return render_template('staffRecords.html')


#Update Pages Note that the POST is to get info, the following makeupdate
#route actually makes the update-----------------------------------------

#If POST, return JSON data of the appoinment corresponding the appointmentid sent with
#response.json.appointmentid
#if GET, render template to corresponding html file
@app.route('/updateAppointments', methods=["GET", "POST"])
def update_appointments():
    if request.method == 'POST':
        #search supabase for data and return, using request data
        return render_template('updateDeleteAppointment.html')
    else:
        return render_template('updateDeleteAppointment.html')

#Update all fields in the request.json object
@app.route('/makeAppointmentUpdate', methods=["POST"])
def updateAppointment():
    if request.method == 'POST':
        #search supabase for data and return, using request data
        print("test")


#If POST, return JSON data of the bill corresponding the billid sent with
#response.json.billid
#if GET, render template to corresponding html file
@app.route('/updateBilling', methods=["GET", "POST"])
def update_billing():
    if request.method == 'POST':
        #search supabase for data and return, using request data
    else:
        return render_template('updateDeleteBill.html')

#Update all fields in the request.json object
@app.route('/makeBillingUpdate', methods=["POST"])
def updateBill():
    if request.method == 'POST':
        #search supabase for data and return, using request data


#If POST, return JSON data of the appoinment corresponding the appointmentid sent with
#response.json.appointmentid
#if GET, render template to corresponding html file
@app.route('/updatePatients', methods=["GET", "POST"])
def update_patients():
    if request.method == 'POST':
        #search supabase for data and return, using request data
    else:
        return render_template('updateDeletePatient.html')

#Update all fields in the request.json object
@app.route('/makePatientUpdate', methods=["POST"])
def updatePatient():
    if request.method == 'POST':
        #search supabase for data and return, using request data



#If POST, return JSON data of the record corresponding the recordid sent with
#response.json.recordid
#if GET, render template to corresponding html file
@app.route('/updateRecords', methods=["GET", "POST"])
def update_billing():
    if request.method == 'POST':
        #search supabase for data and return, using request data
    else:
        return render_template('updateDeleteRecord.html')

#Update all fields in the request.json object
@app.route('/makeRecordUpdate', methods=["POST"])
def updateRecord():
    if request.method == 'POST':
        #search supabase for data and return, using request data

#ID search and Nav Bars--------------------------------------------------------

#The search patients field that takes a name argument and searchis for corresponding fields
# This only returns name and id fields
@app.route('/searchPatients', methods=["POST"]) #Search for only name and id
def searchPatients():
    name = request.args.get('name')
    search_data = searchByPatientName(name)
    return search_data

#Searches appointments by date (YYYY-MM-DD), returns name, date and appointment id
@app.route('/searchAppointments', methods=["GET", "POST"])
def viewAppointments():
    if request.method == 'POST':
        #send
        name = request.json.name
        # return name, date and appointment id
        search_data = getAppointmentsByDate()
        return
    return render_template('main')

#Navigates to staffPatients if logged in as a staff, else navigates to AdminPatients
@app.route('/workbench', methods=["GET"])
def workbench():

#searches Bills by patient name, request.json.name is the name needed. Return a Json object with
#only name and billid and amount fields
@app.route('/searchBills', methods=["GET", "POST"])
def viewBills:


#Inserting/Creating Pages & Functionalities-------------------------------------

#If post, create the patient, else render the page
@app.route('/createPatient', methods=["GET", "POST"])
def createPatient():
    if request.method == 'POST':
        name = request.form.get('FirstName') + " " + request.form.get('LastName')
        address = request.form.get('Address') + " " + request.form.get('Province') + " " + request.form.get('Country')
        dob = "1999-02-14"
        contact = request.form.get('Number')

        patient_info = {
            'name': name,
            'address': address,
            'dob': dob,
            'contact': contact
        }

        result = addDataPatient(patient_info)

        return render_template("adminPatients.html")
    else:
        return render_template('createPatient.html')

#If post, create the appointment, else render the page
@app.route('/createAppointment', methods=["GET", "POST"])
def createAppointment():
    if request.method == 'POST':
        doctorid = request.form.get('DoctorId')
        patientid = request.form.get('PatientId')
        date = "1999-02-14"
        time = request.form.get('Time')
        purpose = request.form.get('Purpose')

        appointment_info = {
            'doctorid': doctorid,
            'patientid': patientid,
            'date': date,
            'time': time,
            'purpose': purpose
        }

        result = addDataAppointment(appointment_info)
        return render_template("adminAppointments.html")
    else:
        return render_template('createAppointment')

#If post, create the bill, else render the page
@app.route('/createBill', methods=["GET", "POST"])
def createBill():
    if request.method == 'POST':

    else:
        return render_template('createBill')

#If post, create the record, else render the page
@app.route('/createRecord', methods=["GET", "POST"])
def createRecord():
    if request.method == 'POST':

    else:
        return render_template('createRecord')

#Deleting functionality---------------------------------------------------

@app.route('/deleteRecord', methods=['POST'])
def deleteRecord():
    #delete the record that corresponds to record.json.recordid field

    if success:
        return
    return

@app.route('/deleteBill', methods=['POST'])
def deleteBill():
    #delete the bill that corresponds to record.json.billid field

    if success:
        return
    return

@app.route('/deleteAppointment', methods=['POST'])
def deleteAppointment():
    #delete the appointment that corresponds to record.json.appointmentid field

    if success:
        return
    return

@app.route('/deletePatient', methods=['POST'])
def deletePatient():
    #delete the record that corresponds to record.json.patientid field

    if success:
        return
    return

#Todo: We must enforce permissions for roles, if it is not correct, we just redirect home