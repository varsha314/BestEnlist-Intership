# Creating a DB with doctor ID & patients visited
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="My_sqlprofile@123"
)
print(mydb)

dbse = mydb.cursor()
dbse.execute("CREATE DATABASE Doctor")
dbse = mydb.cursor()

dbse.execute("SHOW DATABASES")

for entry in dbse:
  print(entry)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="My_sqlprofile@123",
    database="Doctor"
)

dbse = mydb.cursor()
dbse.execute("CREATE TABLE Doctors(dr_name VARCHAR(255),dr_id VARCHAR(255), Patient_visited VARCHAR(255))")
dbse = mydb.cursor()

dbse.execute("SHOW TABLES")

for i in dbse:
  print(i)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="My_sqlprofile@123",
    database="Doctor"
)

dbse = mydb.cursor()

sql = "INSERT INTO Doctors (dr_name,dr_id , Patient_visited) VALUES (%s,%s,%s)"
val = [
    ('Anu', 'D1', '8'),
    ('Anand', 'D2', '3'),
    ('Bindu', 'D3', '10'),
    ('Carl', 'D4', '0'),
    ('Dev', 'D5', '4'),
    ('Gaira', 'D6', '9'),
    ('Harshith', 'D7', '0'),
    ('Imtiaz', 'D8', '7'),
    ('Jack', 'D9', '0'),
    ('Khan', 'D10', '11'),
    ('Leon', 'D11', '20'),
    ('Manish', 'D12', '0'),
    ('Naina', 'D13', '7'),
    ('Pallavi', 'D14', '6'),
    ('Raina', 'D15', '0'),
    ('Sandhya', 'D16', '1')
]

dbse.executemany(sql, val)

mydb.commit()

print(dbse.rowcount, "Record Inserted in Doctor Table")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="My_sqlprofile@123",
    database="Doctor"
)
mycursor = mydb.cursor()
print("Rows Entered:")
mycursor.execute("SELECT * FROM Doctors")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)



# Getting the doctor(s) who have more than 5 patients visited
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="My_sqlprofile@123",
    database="Doctor"
)
mycursor = mydb.cursor()
print("Doctors with more than 5 visited patients:")
mycursor.execute("SELECT dr_name FROM Doctors where Patient_visited > 5")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)



# Getting the doctor(s) with no patients visit
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="My_sqlprofile@123",
    database="Doctor"
)

mycursor = mydb.cursor()
print("Doctors with no patient visits:")
mycursor.execute("SELECT dr_name FROM Doctors where Patient_visited = 0")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)