import mysql.connector
from mysql.connector import Error
import json


data = json.loads(open('responses.json').read())

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='capstone',
                                         user='root',
                                         password='pineapple')

    mySql_Create_Table_Query = """INSERT INTO aadhar_db (Aadhar_number, Name, Date_of_Birth, Gender, Address, Photo) 
                                    VALUES ("7720 5883 9966","Pranav S Nair","2000-06-23","Male","#181 Sobha onyx","photo.jpeg")"""

    
    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    connection.commit()
    print("Inserted successfully ")


except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")