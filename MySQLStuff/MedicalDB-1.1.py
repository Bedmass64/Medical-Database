import mysql.connector
from mysql.connector import Error

# Function to create a connection to MySQL
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


# Function to create a connection to the 'bedmassdb' database
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

# Function to execute a query in the database
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

# Connect to the 'bedmassdb' database
connection = create_db_connection("localhost", "root", "Bedmass-DB", "bedmass_DB")

# SQL queries for table creation based on the schema provided
create_patient_table = """
CREATE TABLE IF NOT EXISTS Patient (
    PatientID int PRIMARY KEY,
    Name varchar(255) NOT NULL,
    Address varchar(255),
    DOB Date,
    Contact varchar(255)
);
"""

create_doctor_table = """
CREATE TABLE IF NOT EXISTS Doctor (
    DoctorID int PRIMARY KEY,
    Name varchar(255) NOT NULL,
    Specialize varchar(255),
    Contact varchar(255),
    Role varchar(255)
);
"""

create_appointment_table = """
CREATE TABLE IF NOT EXISTS Appointment (
    AppointmentID int PRIMARY KEY,
    DoctorID int,
    PatientID int,
    Date Date,
    Time varchar(255),
    Purpose text,
    FOREIGN KEY (DoctorID) REFERENCES Doctor(DoctorID),
    FOREIGN KEY (PatientID) REFERENCES Patient(PatientID)
);
"""

create_medical_history_table = """
CREATE TABLE IF NOT EXISTS Medical_History (
    HistoryID int PRIMARY KEY,
    PatientID int,
    Diagnosis varchar(255),
    Treatment varchar(255),
    Date Date,
    FOREIGN KEY (PatientID) REFERENCES Patient(PatientID)
);
"""

create_billing_table = """
CREATE TABLE IF NOT EXISTS Billing (
    BillID int PRIMARY KEY,
    PatientID int,
    Date Date,
    Amount int,
    PayMethod varchar(255),
    AppointmentID int,
    FOREIGN KEY (PatientID) REFERENCES Patient(PatientID),
    FOREIGN KEY (AppointmentID) REFERENCES Appointment(AppointmentID)
);
"""

create_admin_table = """
CREATE TABLE IF NOT EXISTS Admin (
    AdminID int PRIMARY KEY,
    Name varchar(255) NOT NULL,
    Role varchar(255),
    Contact varchar(255)
);
"""

# Function to insert data into tables
def insert_data(connection, query, values):
    cursor = connection.cursor()
    try:
        cursor.execute(query, values)
        connection.commit()
        print("Data inserted successfully")
    except Error as err:
        print(f"Error: '{err}'")

# # Example data insertion for Patient table
# patient_data = [
#     (1, 'John Doe', '123 Maple Street', '1990-01-01', '555-1234'),
#     (2, 'Jane Smith', '456 Oak Avenue', '1985-05-05', '555-5678'),
# ]
# patient_query = """
# INSERT INTO Patient (PatientID, Name, Address, DOB, Contact)
# VALUES (%s, %s, %s, %s, %s);
# """
# for data in patient_data:
#     insert_data(connection, patient_query, data)

# # Example data insertion for Doctor table
# doctor_data = [
#     (1, 'Dr. Alice Jones', 'Cardiology', '555-2345', 'Attending'),
#     (2, 'Dr. Bob Martin', 'Pediatrics', '555-7890', 'Consultant'),
# ]
# doctor_query = """
# INSERT INTO Doctor (DoctorID, Name, Specialize, Contact, Role)
# VALUES (%s, %s, %s, %s, %s);
# """
# for data in doctor_data:
#     insert_data(connection, doctor_query, data)

# # Example data insertion for Appointment table
# appointment_data = [
#     (1, 1, 2, '2024-02-08', '08:00', 'Regular Checkup'),
#     (2, 2, 1, '2024-02-09', '09:30', 'Follow-up Visit'),
# ]
# appointment_query = """
# INSERT INTO Appointment (AppointmentID, DoctorID, PatientID, Date, Time, Purpose)
# VALUES (%s, %s, %s, %s, %s, %s);
# """
# for data in appointment_data:
#     insert_data(connection, appointment_query, data)

# # Example data insertion for Medical History table
# medical_history_data = [
#     (1, 1, 'Flu', 'Antiviral Medication', '2023-12-01'),
#     (2, 2, 'Allergy', 'Antihistamines', '2024-01-20'),
# ]
# medical_history_query = """
# INSERT INTO Medical_History (HistoryID, PatientID, Diagnosis, Treatment, Date)
# VALUES (%s, %s, %s, %s, %s);
# """
# for data in medical_history_data:
#     insert_data(connection, medical_history_query, data)

# # Example data insertion for Billing table
# billing_data = [
#     (1, 1, '2024-02-08', 200, 'Credit Card', 1),
#     (2, 2, '2024-02-09', 150, 'Cash', 2),
# ]
# billing_query = """
# INSERT INTO Billing (BillID, PatientID, Date, Amount, PayMethod, AppointmentID)
# VALUES (%s, %s, %s, %s, %s, %s);
# """
# for data in billing_data:
#     insert_data(connection, billing_query, data)

# # Example data insertion for Admin table
# admin_data = [
#     (1, 'Charlie Admin', 'System Admin', '555-3456'),
#     (2, 'Dana Manager', 'Office Manager', '555-6789'),
# ]
# admin_query = """
# INSERT INTO Admin (AdminID, Name, Role, Contact)
# VALUES (%s, %s, %s, %s);
# """
# for data in admin_data:
#     insert_data(connection, admin_query, data)

# Execute table creation queries
# execute_query(connection, create_patient_table)
# execute_query(connection, create_doctor_table)
# execute_query(connection, create_appointment_table)
# execute_query(connection, create_medical_history_table)
# execute_query(connection, create_billing_table)
# execute_query(connection, create_admin_table)


# Function to execute a query and print the results
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

# Read and print all tables and their contents
tables_query = "SHOW TABLES"
tables = execute_read_query(connection, tables_query)

# Loop through all tables and print their contents
for table in tables:
    print(f"Table: {table[0]}")
    query = f"SELECT * FROM {table[0]}"
    rows = execute_read_query(connection, query)
    for row in rows:
        print(row)
    print("\n")  # Prints a newline for better readability between tables


