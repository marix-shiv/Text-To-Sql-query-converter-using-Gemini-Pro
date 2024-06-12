import sqlite3

#Connection
connection = sqlite3.connect("student.db")

##Create a cursor to insert create and retrive
cursor = connection.cursor()

##Create table 
table_info = """
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT)

"""

cursor.execute(table_info)

##Insert some more records
cursor.execute("INSERT INTO STUDENT VALUES('Rahul','Data Science','A',100)")
cursor.execute("INSERT INTO STUDENT VALUES('Rohit', 'Data Science', 'B', 90)")
cursor.execute("INSERT INTO STUDENT VALUES('Raj', 'Data Science', 'C', 80)")
cursor.execute("INSERT INTO STUDENT VALUES('Rohan', 'Devops', 'D', 70)")
cursor.execute("INSERT INTO STUDENT VALUES('Rakesh', 'Devops', 'E', 60)")

##Display all records

print("The inserted records are")
data = cursor.execute("SELECT * FROM STUDENT")

for row in cursor:
    print(row)

##Close the connection
connection.commit()
connection.close()