

# def readTableData(tableName: str): #JSON into HTML 
#     getConnection()
#     response = supabase.table(tableName).select("*").execute()
#     print(f"{tableName} response: ",response)
#     return response

# readTableData("patient")

# def filterTable(tableName: str, row: str, rowValue): #JSON into HTML
#     response = supabase.table(tableName).select("*").eq(row, rowValue).execute()
#     print(response)
#     return response


# def getAppointmentsByDate(date_str: str): #JSON into HTML 
#     # Ensure the input date is in the correct format (YYYY-MM-DD)
#     try:
#         desired_date = datetime.strptime(date_str, '%Y-%m-%d').date()
#     except ValueError:
#         print("Incorrect date format, should be YYYY-MM-DD")
#         return None

#     # Query to select all appointments
#     response = supabase.table('appointment').select("*").execute()

#     # Check if data is present in the response
#     if not response.data:  # Simplified error handling
#         print("No data found or error in fetching appointments")
#         return None

#     # Filter appointments by date on the client side
#     appointments_on_date = [
#         appointment for appointment in response.data
#         if 'date' in appointment and datetime.strptime(appointment['date'], '%Y-%m-%dT%H:%M:%S+00:00').date() == desired_date
#     ]
    
#     print(appointments_on_date)
#     return appointments_on_date