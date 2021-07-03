import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="My_sqlprofile@123",
)

mycursor = mydb.cursor()
print(mydb)

dbse = mydb.cursor()

dbse.execute("CREATE DATABASE Employee_Mangement")
dbse = mydb.cursor()

dbse.execute("SHOW DATABASES")

for entry in dbse:
    print(entry)



# Creating an Employee Table with employee name,employee ID & Salary
mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="My_sqlprofile@123",
  database="employee_mangement"
)
dbse = mydb.cursor()

dbse.execute("CREATE TABLE Employee (emp_id INT , EMP_NAME VARCHAR(255),EMP_SALARY DOUBLE )")

dbse = mydb.cursor()

dbse.execute("SHOW TABLES")

for value in dbse:
  print(value)

dbse = mydb.cursor()

dbse.execute("SHOW COLUMNS FROM Employee")

for value in dbse:
  print(value)

dbse = mydb.cursor()

sql = "INSERT INTO Employee (emp_id , EMP_NAME , EMP_SALARY) VALUES (%s,%s,%s)"
val = [
    ('101', 'ALI', '10000'),
    ('102', 'ANU', '15000'),
    ('103', 'BINDU', '70000'),
    ('104', 'KAVYA', '80000'),
    ('105', 'RAJ', '80000'),
    ('106', 'SATHEESH', '50000'),
    ('107', 'MUNA', '60000'),
    ('108', 'JACK', '70000'),
    ('109', 'MAYA', '30000'),
    ('110', 'VANI', '15000'),
    ('111', 'LAKSHMI', '50000'),
    ('112', 'PREMA', '40000'),
    ('113', 'KAMAL', '25000'),
    ('114', 'MADHAV', '30000'),
    ('115', 'YARAAN', '100000')

]

dbse.executemany(sql, val)

mydb.commit()

print(dbse.rowcount, "was inserted.")




# Writing a query to get the maximum and minimum salary from employees table
mycursor = mydb.cursor()

mycursor.execute("SELECT EMP_NAME,EMP_SALARY FROM Employee where EMP_SALARY = (select max(EMP_SALARY) from Employee)")

myresult = mycursor.fetchall()
print("Maximum Salary:")
for x in myresult:
    print(x)

mycursor = mydb.cursor()

mycursor.execute("SELECT EMP_NAME,EMP_SALARY FROM employee where EMP_SALARY = (select min(EMP_SALARY) from Employee)")

myresult = mycursor.fetchall()
print("Minimum Salary:")
for x in myresult:
    print(x)




# Writing a query to get the number of employees working with the company
mycursor = mydb.cursor()

mycursor.execute("SELECT COUNT(*) from Employee")

myresult = mycursor.fetchall()
print("Number of Employees:")
for x in myresult:
    print(x)



# Writing a query to get the first 3 characters of first name from employees table
mycursor = mydb.cursor()

mycursor.execute("SELECT SUBSTRING(EMP_NAME,1,3) FROM Employee")

myresult = mycursor.fetchall()
print("First 3 letters of name:")
for x in myresult:
    print(x)