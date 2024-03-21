
# Continue this tutorial the next time you work on this
# https://blog.pythonanywhere.com/121/

from flask import Flask, redirect, render_template, request, url_for, jsonify
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
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


#RESTFUL API Endoints------------------------------------------------

#READ ENDPOINTS
@app.route('/api/patients', methods=["GET"])
def get_all_patients():
    return readTableData("patient")

@app.route('/api/patients/id', methods=["GET"])
def get_patient_by_id():
    id = request.args.get('id')
    if id:
        return filterTable("patient", "patientid", id)
    else:
        return "Id parameter is missing", 400

@app.route('/api/patients/name', methods=["GET"])
def get_patient_by_name():
    name = request.args.get('name')
    if name:
        return filterTable("patient", "name", name)
    else:
        return "Name parameter is missing", 400

@app.route('/api/appointments', methods=["GET"])
def get_all_appointments():
    return readTableData("appointment")

@app.route('/api/appointments/id', methods=["GET"])
def get_appointment_by_id():
    id = request.args.get('id')
    if id:
        return filterTable("appointment", "appointmentid", id)
    else:
        return "Id parameter is missing", 400

@app.route('/api/appointments/date', methods=["GET"])
def get_appointment_by_date():
    date = request.args.get('date')
    if date:
        return getAppointmentsByDate(date)
    else:
        return "Date parameter is missing", 400

@app.route('/api/bills', methods=["GET"])
def get_all_bills():
    return readTableData("billing")

@app.route('/api/bills/id', methods=["GET"])
def get_bill_by_id():
    id = request.args.get('id')
    if id:
        return filterTable("billing", "billid", id)
    else:
        return "Id parameter is missing", 400

@app.route('/api/bills/patientid', methods=["GET"])
def get_bill_by_patient_id():
    id = request.args.get('id')
    if id:
        return filterTable("billing", "patientid", id)
    else:
        return "Name parameter is missing", 400

@app.route('/api/records', methods=["GET"])
def get_all_records():
    return readTableData("medical_history")

@app.route('/api/records/id', methods=["GET"])
def get_record_by_id():
    id = request.args.get('id')
    if id:
        return filterTable("medical_history", "historyid", id)
    else:
        return "Id parameter is missing", 400

@app.route('/api/records/patientid', methods=["GET"])
def get_record_by_patient_id():
    id = request.args.get('id')
    if id:
        return filterTable("medical_history", "patientid", id)
    else:
        return "Name parameter is missing", 400


#Table Formats: JSON
#patient:
# {
#   "patientid": "int",
#   "name": "string",
#   "address": "string",
#   "dob": "date",
#   "contact": "string"
# }


#appointment:
#{
#   "appointmentid": "int",
#   "doctorId": "int",
#   "patientId": "int",
#   "date": "date",
#   "time": "string",
#   "purpose": "string"
#}

#billing:
# {
#   "billid": "int",
#   "patientid": "int",
#   "date": "timestamp with time zone",
#   "amount": "int",
#   "paymethod": "string",
#   "appointmentid": "int",
#   "payconfirmed": "bool"
# }

#medical_history:
# {
#   "historyid": "int",
#   "patientid": "int",
#   "diagnosis": "string",
#   "treatment": "string",
#   "date": "timestamp with time zone"
# }


#Create Endpoints
@app.route('/api/patients', methods=["POST"])
def create_patient():
    data = request.json
    result = addDataPatient(data)
    return jsonify(result)

@app.route('/api/appointments', methods=["POST"])
def create_appointment():
    data = request.json
    result = addDataAppointment(data)
    return jsonify(result)

@app.route('/api/bills', methods=["POST"])
def create_bill():
    data = request.json
    result = addDataBilling(data)
    return jsonify(result)

@app.route('/api/records', methods=["POST"])
def create_record():
    data = request.json
    result = addDataMedicalHistory(data)
    return jsonify(result)


#Update Endpoints
@app.route('/api/patients', methods=["PUT"])
def update_patient():
    data = request.json
    result = updateDataPatient(data)
    return jsonify(result)

@app.route('/api/appointments', methods=["PUT"])
def update_appointment():
    data = request.json
    result = updateDataAppointment(data)
    return jsonify(result)

@app.route('/api/bills', methods=["PUT"])
def update_bill():
    data = request.json
    result = updateDataBilling(data)
    return jsonify(result)

@app.route('/api/records', methods=["PUT"])
def update_record():
    data = request.json
    result = updateDataMedicalHistory(data)
    return jsonify(result)



#Delete Endpoints
@app.route('/api/patients', methods=["DELETE"])
def delete_patient():
    id = request.args.get('id')
    result = deleteDataPatient(id)
    return jsonify(result)

@app.route('/api/appointments', methods=["DELETE"])
def delete_appointment():
    id = request.args.get('id')
    result = deleteDataAppointment(id)
    return jsonify(result)

@app.route('/api/bills', methods=["DELETE"])
def delete_bill():
    id = request.args.get('id')
    result = deleteDataBilling(id)
    return jsonify(result)

@app.route('/api/records', methods=["DELETE"])
def delete_record():
    id = request.args.get('id')
    result = deleteDataMedicalHistory(id)
    return jsonify(result)


#Create Account-----------------------------------------------------

#For POST, login with fields stated below. If success, log user in and create an account and
#redirect to main page. If not, throw an error
#For GET, render the create html page
@app.route('/createAccount', methods=["GET", "POST"])
def createAccount():
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
def adminPatients():
    if request.method == 'POST':
        #search supabase for data and return, using request data
        name = request.json['name']
        if(name == ""):
            return readTableData("patient")
        return filterTableData("patient", "name", name)

    else:
        return render_template('adminPatients.html')

#If POST, return JSON data of the billing corresponding the patientid sent with
#response.json.patientid
#if GET, render template to corresponding html file
@app.route('/adminBilling', methods=["GET", "POST"])
def adminBilling():
    if request.method == 'POST':
        #search supabase for data and return, using request data
        return render_template('adminBilling.html')
    else:
        return render_template('adminBilling.html')

#If POST, return JSON data of the records corresponding the patientid sent with
#response.json.patientid
#if GET, render template to corresponding html file
@app.route('/adminRecords', methods=["GET", "POST"])
def adminRecords():
    if request.method == 'POST':
        #search supabase for data and return, using request data
        return render_template('adminRecords.html')

    else:
        return render_template('adminRecords.html')

#If POST, return JSON data of the appointemnts corresponding the date sent with
#response.json.date in (YYYY-MM-DD) format
#if GET, render template to corresponding html file
@app.route('/adminAppointments', methods=["GET", "POST"])
def adminAppointments():
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
def staffPatients():
    if request.method == 'POST':
        #search supabase for data and return, using request data

        return render_template('staffPatients.html')

    else:
        return render_template('staffPatients.html')

#If POST, return JSON data of the appointemnts corresponding the date sent with
#response.json.date in (YYYY-MM-DD) format
#if GET, render template to corresponding html file
@app.route('/staffAppointments', methods=["GET", "POST"])
def staffAppointments():
    if request.method == 'POST':
        #search supabase for data and return, using request data
        #Search by DATE
        return render_template('staffAppointments.html')

    else:
        return render_template('staffAppointments.html')


#If POST, return JSON data of the records corresponding the patientid sent with
#response.json.patientid
#if GET, render template to corresponding html file
@app.route('/staffRecords', methods=["GET", "POST"])
def staffRecords():
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
def updateAppointments():
    if request.method == 'POST':
        #search supabase for data and return, using request data
        return render_template('updateDeleteAppointment.html')
    else:
        return render_template('updateDeleteAppointment.html')

#Update all fields in the request.json object
@app.route('/makeAppointmentUpdate', methods=["POST"])
def makeAppointmentUpdate():
    if request.method == 'POST':
        #search supabase for data and return, using request data
        print("test")


#If POST, return JSON data of the bill corresponding the billid sent with
#response.json.billid
#if GET, render template to corresponding html file
@app.route('/updateBilling', methods=["GET", "POST"])
def updateBilling():
    if request.method == 'POST':
        #search supabase for data and return, using request data
        return render_template('updateDeleteBill.html')
    else:
        return render_template('updateDeleteBill.html')

#Update all fields in the request.json object
@app.route('/makeBillingUpdate', methods=["POST"])
def makeBillingUpdate():
    if request.method == 'POST':
        #search supabase for data and return, using request data
        print("Make billing update")


#If POST, return JSON data of the appoinment corresponding the appointmentid sent with
#response.json.appointmentid
#if GET, render template to corresponding html file
@app.route('/updatePatients', methods=["GET", "POST"])
def updatePatients():
    if request.method == 'POST':
        #search supabase for data and return, using request data
        return render_template('updateDeletePatient.html')
    else:
        return render_template('updateDeletePatient.html')

#Update all fields in the request.json object
@app.route('/makePatientUpdate', methods=["POST"])
def makePatientUpdate():
    if request.method == 'POST':
        #search supabase for data and return, using request data
        return render_template('updateDeleteRecord.html')



#If POST, return JSON data of the record corresponding the recordid sent with
#response.json.recordid
#if GET, render template to corresponding html file
@app.route('/updateRecords', methods=["GET", "POST"])
def updateRecords():
    if request.method == 'POST':
        #search supabase for data and return, using request data
        return render_template('updateDeleteRecord.html')
    else:
        return render_template('updateDeleteRecord.html')

#Update all fields in the request.json object
@app.route('/makeRecordUpdate', methods=["POST"])
def makeRecordUpdate():
    if request.method == 'POST':
        #search supabase for data and return, using request data
        return render_template('updateDeleteRecord.html')

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
def searchAppointments():
    if request.method == 'POST':
        #send
        name = request.json.name
        # return name, date and appointment id
        search_data = getAppointmentsByDate()
        return render_template('main.html')
    return render_template('main.html')

#Navigates to staffPatients if logged in as a staff, else navigates to AdminPatients
@app.route('/workbench', methods=["GET"])
def workbench():
    print("workbench")

#searches Bills by patient name, request.json.name is the name needed. Return a Json object with
#only name and billid and amount fields
@app.route('/searchBills', methods=["GET", "POST"])
def searchBills():
    print("view bills")

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
        return render_template('createAppointment.html')

#If post, create the bill, else render the page
@app.route('/createBill', methods=["GET", "POST"])
def createBill():
    if request.method == 'POST':
        return render_template('createBill.html')
    else:
        return render_template('createBill.html')

#If post, create the record, else render the page
@app.route('/createRecord', methods=["GET", "POST"])
def createRecord():
    if request.method == 'POST':
        return render_template('createRecord.html')
    else:
        return render_template('createRecord.html')

#Deleting functionality---------------------------------------------------

@app.route('/deleteRecord', methods=['POST'])
def deleteRecord():
    #delete the record that corresponds to record.json.recordid field

    if success:
        return 1
    return 1

@app.route('/deleteBill', methods=['POST'])
def deleteBill():
    #delete the bill that corresponds to record.json.billid field

    if success:
        return 1
    return 1

@app.route('/deleteAppointment', methods=['POST'])
def deleteAppointment():
    #delete the appointment that corresponds to record.json.appointmentid field

    if success:
        return 1
    return 1

@app.route('/deletePatient', methods=['POST'])
def deletePatient():
    #delete the record that corresponds to record.json.patientid field

    if success:
        return 1
    return 1

#Todo: We must enforce permissions for roles, if it is not correct, we just redirect home
