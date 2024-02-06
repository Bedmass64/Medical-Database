import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Bedmass-DB",
    database = "bedmassdb"
)

cursor = db.cursor()

#Billing table 
#Billing Values and Datatypes:
#BillID int, PatientID int, Date Date, Amount int, PayMethod varchar, AppointmentID int

# cursor.execute("CREATE TABLE Billing (BillID varchar(50), Date Date, Amount int, PayMethod varchar(50), AppointmentID int)")
# cursor.execute("INSERT INTO Billing(PatientID, Date, Amount, PayMethod, AppointmentID)", 0000, "2024-02-05", 1200.00, )