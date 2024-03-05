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


def addDataPatient(tableName: str, data: dict):
    supabase.table(tableName).insert(data).execute()
    print("Data added to table: " + tableName)
        
# addDataPatient(tableName, data)

def readTableData(tableName: str):
    response = supabase.table(tableName).select("*").execute()
    print(f"{tableName} response: ",response)

supabase.table('billing').update({'amount': 400}).eq('billid',15).execute()

def updateRow(tableName: str, coloum: str, value, row: str, rowValue):
    supabase.table(tableName).update({coloum:value}).eq(row, rowValue).execute()
    print("Data added to " + tableName)

def deleteRow(tableName: str, row: str, rowValue):
    supabase.table(tableName).delete().eq(row,rowValue).execute()
    print(f"Data row {rowValue} deleted from " + tableName)

def filterTable(tableName: str, row: str, rowValue):
    response = supabase.table(tableName).select("*").eq(row, rowValue).execute()
    print(response)

#updateRow('billing', 'amount', 400, 'billid', 15)
#deleteRow('billing', 'billid',16)
#readTableData("patient")
# filterTable('billing','billid',16)
readTableData("doctor")
# response = supabase.table('billing').select("*").execute()
# print(response)