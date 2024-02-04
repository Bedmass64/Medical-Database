import mysql.connector

# db = mysql.connector.connect()

db = mysql.connector.connect(
    host="localhost", #Connects to this computer, not another one
    user="root",
    passwd="Bedmass-DB",
    database="medicaldb"
)

cursor = db.cursor()
