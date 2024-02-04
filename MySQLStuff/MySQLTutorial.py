import mysql.connector

# db = mysql.connector.connect()

db = mysql.connector.connect(
    host="localhost", #Connects to this computer, not another one
    user="root",
    passwd="Bedmass-DB",
    database="medicaldb"
)

cursor = db.cursor()

# cursor.execute("CREATE DATABASE medicaldb")

## Creating some tables, creating some coloums, and then adding entryies in. 
## Creating first table

#cursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
#cursor.execute("INSERT INTO Person(name, age) VALUES (%s,%s)", ("Josh", 20))
#db.commit()

cursor.execute("SELECT * FROM Person") #Selects all from the table person and gives it to us

for x in cursor:
    print(x)



# Primary Key is the unique number for every single person, 
# it's generated and different everytime an element is added
