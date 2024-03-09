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


table_format = "<table class='table table-hover table-primary table-bordered table-striped'>"

#
#     WRITING FUNCTIONS:
#
def getConnection():
    supabase: Client = create_client(url, key)


def addDataPatient(data: dict):
    getConnection()
    supabase.table("patient").insert(data).execute()
    return "Data added to table"

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

#
#     UPDATE FUNCTIONS:
#

def updateDataAppointment(appointmentid: int, updates: dict):
    # Filter out any keys where the value is None (null)
    filtered_updates = {k: v for k, v in updates.items() if v is not None}

    # Execute the update operation with the filtered updates
    response = supabase.table("appointment").update(filtered_updates).eq("appointmentid", appointmentid).execute()

    # Print result
    print("Data updated for table appointment")

# updateDataAppointment(3, {'time': '12:40'})

def updateDataBilling(billid: int, updates: dict):
    filtered_updates = {k: v for k, v in updates.items() if v is not None}
    response = supabase.table("billing").update(filtered_updates).eq("billid", billid).execute()
    print("Billing data updated")

#updateDataBilling(15,{'payconfirmed': True })

def updateDataDoctor(doctorid: int, updates: dict):
    filtered_updates = {k: v for k, v in updates.items() if v is not None}
    response = supabase.table("doctor").update(filtered_updates).eq("doctorid", doctorid).execute()
    print("Doctor data updated")

# updateDataDoctor(2, {'role':'Staff Director'})

def updateDataMedicalHistory(historyid: int, updates: dict):
    filtered_updates = {k: v for k, v in updates.items() if v is not None}
    response = supabase.table("medical_history").update(filtered_updates).eq("historyid", historyid).execute()
    print("Medical history data updated")

# updateDataMedicalHistory(2,{'treatment':'kimotheirpy'})

def updateDataAdmin(adminid: int, updates: dict):
    filtered_updates = {k: v for k, v in updates.items() if v is not None}
    response = supabase.table("admin").update(filtered_updates).eq("adminid", adminid).execute()
    print("Admin data updated")

# updateDataAdmin(2,{'role': 'Skilled Awesome Person'})

def updateDataPatient(patientid: int, updates: dict):
    # Filter out any keys where the value is None (null)
    filtered_updates = {k: v for k, v in updates.items() if v is not None}

    # Assuming getConnection is called if needed
    # getConnection()

    # Execute the update operation with the filtered updates
    response = supabase.table("patient").update(filtered_updates).eq("patientid", patientid).execute()

    # Check if the update was successful based on the response structure
    if hasattr(response, 'status_code') and response.status_code == 200:
        print(f"Data updated for patientid {patientid}")
    elif hasattr(response, 'data') and response.data:
        # Assuming the update is successful if there's data (adjust based on actual response structure)
        print(f"Data updated for patientid {patientid}")
    else:
        # If the response structure is different, adjust this part accordingly
        print("Error updating data")

# updateDataPatient(2, {"name": "Ben Impostor Lupin"})

#
#     DELETE FUNCTIONS:
#
        
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

#
# OTHER FUNCTIONS
#
    
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
    html_output = table_format  # Start the table and add headers

    # Add column headers based on the first item keys if there's data
    if response.data:
        html_output += '<tr>' + ''.join([f'<th>{col.capitalize()}</th>' for col in response.data[0].keys()]) + '</tr>'

        # Fill the table rows with the data
        for item in response.data:
            html_output += '<tr>' + ''.join([f'<td>{item[col]}</td>' for col in item.keys()]) + '</tr>'

    html_output += "</table>"  # Close the table
    print(html_output)  # Print the HTML table
    return html_output

# Test the function
readTableData("patient")


def updateRow(tableName: str, coloum: str, value, row: str, rowValue):
    supabase.table(tableName).update({coloum:value}).eq(row, rowValue).execute()
    print("Data added to " + tableName)

def deleteRow(tableName: str, row: str, rowValue):
    supabase.table(tableName).delete().eq(row,rowValue).execute()
    print(f"Data row {rowValue} deleted from " + tableName)



def filterTable(tableName: str, row: str, rowValue):
    getConnection()
    response = supabase.table(tableName).select("*").eq(row, rowValue).execute()

    # Check if data is present in the response
    if not response.data:  # Simplified error handling
        print("No data found or error in fetching data")
        return None

    # Construct HTML table from response data
    html_output = table_format  # Start the table and add headers

    # Add column headers based on the first item keys if there's data
    if response.data:
        html_output += '<tr>' + ''.join([f'<th>{col.capitalize()}</th>' for col in response.data[0].keys()]) + '</tr>'

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

    # Construct HTML table
    if appointments_on_date:
        html_output = table_format
        html_output += "<tr><th>Appointment ID</th><th>Doctor ID</th><th>Patient ID</th><th>Date</th><th>Time</th><th>Purpose</th></tr>"

        for appointment in appointments_on_date:
            html_output += f"<tr><td>{appointment['appointmentid']}</td><td>{appointment['doctorid']}</td><td>{appointment['patientid']}</td><td>{appointment['date']}</td><td>{appointment['time']}</td><td>{appointment['purpose']}</td></tr>"

        html_output += "</table>"
        print(html_output)  # Print the HTML table
        return html_output
    else:
        print("No appointments found on the specified date")
        return None

#Create update functions for each table
# Test the function
# getAppointmentsByDate('2024-02-24')


#Some functions for processing the data we get from supabase into a string that's formatted into an HTML table Done
#Add functions for update (Delete functions)
#When a row is updated, check to see which attributes are actually being updated and just update those attributes

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