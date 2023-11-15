

#first install mysql ,install connector 
#install package for mysql for connecting
# if can't see some lecture


"""
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="give your password"
)

mycursor=mydb.cursor()

mycursor.execute("CREATE DATABASE pythonprogramming")


"""
#to show database from here

"""
mycursor.execute("SHOW DATABASE")

for x in mycursor:
    print(x)
"""


#CREATE TABLE -------------------------------


"""
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="give your password",
    database="pythonprogramming"
)

mycursor=mydb.cursor()

mycursor.execute("CREATE TABLE customer(name varchar(255),address varchar(255))")


"""

#to show table ------------

"""
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

"""

#print details from table 

"""
mycursor.execute("SELECT * FROM actor")

myres=mycursor.fetchall() 

for x in myres:
    print(x)

"""
#--->>>fecthall use to print all details from table


#to fetch and print one row use fetchone()

"""
myres=mycursor.fetchone()

print(myres)

"""


"""
 TO KNOW MORE ABOUT THIS GO TO MYSQL DOCUMENTATION AND STUDY
  
"""