import mysql.connector
from datetime import datetime
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

cursor.execute("SELECT * FROM Test") #Selects all from the table person and gives it to us

for x in cursor:
    print(x)



# cursor.execute("CREATE TABLE Test (name varchar(50) NOT NULL, created datetime NOT NULL, sex ENUM('M', 'F') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")


# cursor.execute("INSERT INTO Test(name, created, sex) VALUES (%s, %s, %s)", ("BEN", datetime.now(), "M"))

# cursor.execute("SELECT * FROM Test WHERE sex = 'M'")

# db.commit()

# Primary Key is the unique number for every single person, 
# it's generated and different everytime an element is added
