from supabase import create_client, Client
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

#
#     DELETING FUNCTIONS:
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






def readTableData(tableName: str):
    getConnection()
    response = supabase.table(tableName).select("*").execute()
    print(f"{tableName} response: ",response)
    return response

#supabase.table('billing').update({'amount': 400}).eq('billid',15).execute()

def updateRow(tableName: str, coloum: str, value, row: str, rowValue):
    supabase.table(tableName).update({coloum:value}).eq(row, rowValue).execute()
    print("Data added to " + tableName)

def deleteRow(tableName: str, row: str, rowValue):
    supabase.table(tableName).delete().eq(row,rowValue).execute()
    print(f"Data row {rowValue} deleted from " + tableName)

def filterTable(tableName: str, row: str, rowValue):
    response = supabase.table(tableName).select("*").eq(row, rowValue).execute()
    print(response)
    return response

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


#searchByUsernameDoctor("IAmDoingWork0_0")
#searchByUsernameAdmin("login1")

#SearchByUsernameFunctionForDocotor:Returns Password
#SearchByUsernameFunctionForAdmin: Returns Password 
#FilterAppointmentFunction by Date: Returns Appointments
#SearchFunction

#AllReadFuncitons Return output 
#updateRow('admin', 'password', 'password2', 'adminid', 2)
#deleteRow('billing', 'billid',16)
#readTableData("patient")
# filterTable('billing','billid',16)
#readTableData("admin")
# response = supabase.table('billing').select("*").execute()
# print(response)