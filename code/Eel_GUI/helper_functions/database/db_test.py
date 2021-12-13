import mysql.connector
from mysql.connector import Error
import json

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='capstone',
                                         user='root',
                                         password='pineapple')
        
    mySql_Create_Table_Query = """CREATE TABLE  form_questions_test (
                        First_name varchar(250),
                        Last_name varchar(250),
                        Category varchar(250), 
                        Photo BLOB,
                        Disability_Certificate varchar(250),
                        Disability_type varchar(250),
                        Aadhar_number varchar(250) NOT NULL PRIMARY KEY)"""
            


    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Laptop Table created successfully ")


except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")