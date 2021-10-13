import mysql.connector
from mysql.connector import Error
import json


data = json.loads(open('responses.json').read())

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='capstone',
                                         user='root',
                                         password='pineapple')

    mySql_Create_Table_Query = """INSERT INTO form_questions_test (First_name, Last_name, Category, Photo, Disability_Certificate, Disability_type, Aadhar_number) VALUES ("""

    questions = list(data.keys())
    val = []
    for i in range(len(questions)):
        x = "'" +  data[questions[i]] + "'"
        val.append(x)
        
    mySql_Create_Table_Query = mySql_Create_Table_Query +  ",".join(val) + ")"
#print(mySql_Create_Table_Query)

    
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