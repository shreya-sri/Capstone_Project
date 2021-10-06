import mysql.connector
from mysql.connector import Error


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='capstone',
                                         user='root',
                                         password='pineapple')
        
    mySql_Create_Table_Query = """CREATE TABLE  aadhar_db (
                        Aadhar_number varchar(14) NOT NULL PRIMARY KEY,
                        Name varchar(250) NOT NULL,
                        Date_of_Birth DATE NOT NULL,
                        Gender varchar(50) NOT NULL, 
                        Address varchar(250) NOT NULL,
                        Photo BLOB NOT NULL)"""
            


    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Aadhar Table created successfully ")


except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")