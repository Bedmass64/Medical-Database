from supabase import create_client, Client
from datetime import datetime
#Tables include:
#admin, appointment, billing, doctor, medical_history, patient
# print("Hello World")

url: str = "https://rdiogfocbfebfkvoyvoj.supabase.co"
#key: str = "sbp_0df95d125573379f2aee1499a8ad1d3978c70cdf "
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJkaW9nZm9jYmZlYmZrdm95dm9qIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDgwMDUyMTIsImV4cCI6MjAyMzU4MTIxMn0.WX0hS7III4FjNkIvaPCpN0zovU88i2UaRdCdHBr-P8o"
supabase: Client = create_client(url, key)
# tableName: str = "patient"
# data: dict = {"patientid": 3948, "name": "Joe Shmoe", "address": "123 Hamburger ln", "dob": "1999-12-12", "contact": "123-456-7890"}

#
#     WRITING FUNCTIONS:
#
def getConnection():
    supabase: Client = create_client(url, key)


def addDataPatient(data: dict):
    supabase.table("patient").insert(data).execute()
    print("Data added to table")

def addDataAppointment(data: dict):
    supabase.table("appointment").insert(data).execute()
    print("Data added to table")

def addDataBilling(data: dict):
    supabase.table("billing").insert(data).execute()
    print("Data added to table")

def addDataDoctor(data: dict):
    supabase.table("doctor").insert(data).execute()
    print("Data added to table")

def addDataMedicalHistory(data: dict):
    supabase.table("medical_history").insert(data).execute()
    print("Data added to table")

def addDataAdmin(data: dict):
    supabase.table("admin").insert(data).execute()
    print("Data added to table")

def deleteDataPatient(patientid: int):
    supabase.table("patient").delete().eq("patientid", patientid).execute()
    print("Data deleted from table")

def deleteDataAppointment(appointmentid: int):
    supabase.table("appointment").delete().eq("appointmentid", appointmentid).execute()
    print("Data deleted from table")

def deleteDataBilling(billid: int):
    supabase.table("billing").delete().eq("billid", billid).execute()
    print("Data deleted from table")

def deleteDataDoctor(doctorid: int):
    supabase.table("doctor").delete().eq("doctorid", doctorid).execute()
    print("Data deleted from table")

def deleteDataMedicalHistory(historyid: int):
    supabase.table("medical_history").delete().eq("historyid", historyid).execute()
    print("Data deleted from table")

def deleteDataAdmin(adminid: int):
    supabase.table("admin").delete().eq("adminid", adminid).execute()
    print("Data deleted from table")



def readTableData(tableName: str):
    # Assuming getConnection() establishes your database connection
    getConnection()  
    # Perform the database query
    response = supabase.table(tableName).select("*").execute()

    # Check if data is present in the response
    if not response.data:  # Simplified error handling
        print(f"No data found or error in fetching data from {tableName}")
        return None

    # Construct HTML table from response data
    html_output = "<table border='1'>"  # Start the table and add headers

    # Add column headers based on the first item keys if there's data
    if response.data:
        html_output += '<tr>' + ''.join([f'<th>{col}</th>' for col in response.data[0].keys()]) + '</tr>'

        # Fill the table rows with the data
        for item in response.data:
            html_output += '<tr>' + ''.join([f'<td>{item[col]}</td>' for col in item.keys()]) + '</tr>'

    html_output += "</table>"  # Close the table
    print(html_output)  # Print the HTML table
    return html_output

# Test the function
readTableData("doctor")


def updateRow(tableName: str, coloum: str, value, row: str, rowValue):
    supabase.table(tableName).update({coloum:value}).eq(row, rowValue).execute()
    print("Data added to " + tableName)

def deleteRow(tableName: str, row: str, rowValue):
    supabase.table(tableName).delete().eq(row,rowValue).execute()
    print(f"Data row {rowValue} deleted from " + tableName)



def filterTable(tableName: str, row: str, rowValue):
<<<<<<< HEAD
    # Perform the database query
=======
    getConnection()
>>>>>>> 99e3efb0d5c47b92218e85e0a40a9d987b61a874
    response = supabase.table(tableName).select("*").eq(row, rowValue).execute()

    # Check if data is present in the response
    if not response.data:  # Simplified error handling
        print("No data found or error in fetching data")
        return None

    # Construct HTML table from response data
    html_output = "<table border='1'>"  # Start the table and add headers

    # Add column headers based on the first item keys if there's data
    if response.data:
        html_output += '<tr>' + ''.join([f'<th>{col}</th>' for col in response.data[0].keys()]) + '</tr>'

        # Fill the table rows with the data
        for item in response.data:
            html_output += '<tr>' + ''.join([f'<td>{item[col]}</td>' for col in item.keys()]) + '</tr>'

    html_output += "</table>"  # Close the table
    print(html_output)  # Print the HTML table
    return html_output

# # Test the function
# filterTable('billing', 'billid', 15)

def searchByUsernameDoctor(Username: str):
    response = supabase.table('doctor').select("password").eq('login', Username).execute()
    # Extracting password from response
    password = response.data[0]['password'] if response.data else None
    print(password)
    return password


def searchByUsernameAdmin(Username: str):
    response = supabase.table('admin').select("password").eq('login', Username).execute()
    # Extracting password from response
    password = response.data[0]['password'] if response.data else None
    print(password)
    return password


def getAppointmentsByDate(date_str: str):  # JSON into HTML
    from datetime import datetime  # Make sure to import datetime

    # Ensure the input date is in the correct format (YYYY-MM-DD)
    try:
        desired_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        print("Incorrect date format, should be YYYY-MM-DD")
        return None

    # Your existing code for fetching and filtering appointments here...
    # Query to select all appointments
    response = supabase.table('appointment').select("*").execute()

    # Check if data is present in the response
    if not response.data:  # Simplified error handling
        print("No data found or error in fetching appointments")
        return None

    # Filter appointments by date on the client side
    appointments_on_date = [
        appointment for appointment in response.data
        if 'date' in appointment and datetime.strptime(appointment['date'], '%Y-%m-%dT%H:%M:%S+00:00').date() == desired_date
    ]

<<<<<<< HEAD
    # Construct HTML table
    if appointments_on_date:
        html_output = "<table border='1'>"
        html_output += "<tr><th>Appointment ID</th><th>Doctor ID</th><th>Patient ID</th><th>Date</th><th>Time</th><th>Purpose</th></tr>"

        for appointment in appointments_on_date:
            html_output += f"<tr><td>{appointment['appointmentid']}</td><td>{appointment['doctorid']}</td><td>{appointment['patientid']}</td><td>{appointment['date']}</td><td>{appointment['time']}</td><td>{appointment['purpose']}</td></tr>"

        html_output += "</table>"
        print(html_output)  # Print the HTML table
        return html_output
    else:
        print("No appointments found on the specified date")
        return None

# Test the function
# getAppointmentsByDate('2024-02-24')
=======
    print(appointments_on_date)
    return appointments_on_date
>>>>>>> 99e3efb0d5c47b92218e85e0a40a9d987b61a874


#Some functions for processing the data we get from supabase into a string that's formatted into an HTML table 
#Add coloums for update and delete

#searchByUsernameDoctor("IAmDoingWork0_0")
#searchByUsernameAdmin("login1")

#SearchByUsernameFunctionForDocotor:Returns Password Done
#SearchByUsernameFunctionForAdmin: Returns Password Done
#FilterAppointmentFunction by Date: Returns Appointments Done
#SearchFunction ?

#AllReadFuncitons Return output
#updateRow('admin', 'password', 'password2', 'adminid', 2)
#deleteRow('billing', 'billid',16)
#readTableData("patient")
# filterTable('billing','billid',16)
# readTableData("appointment")
# response = supabase.table('billing').select("*").execute()
# print(response)