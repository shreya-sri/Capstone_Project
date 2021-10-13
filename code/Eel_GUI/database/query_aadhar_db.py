import mysql.connector
from mysql.connector import Error



def queryAadhar(aadhar_number):
    results=0
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='capstone_project',
                                            user='root')
                                            #password='pineapple')
        
        mySql_Create_Table_Query = """SELECT * FROM aadhar_db WHERE  Aadhar_number = '{}'""".format(aadhar_number)

        cursor = connection.cursor()
        cursor.execute(mySql_Create_Table_Query)
        results = cursor.fetchall()
        print("Aadhar Table queried successfully ")
        


    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        #print("in finally")
        if connection.is_connected():
            cursor.close()
            connection.close()
            print(results)
            print("MySQL connection is closed")

if __name__=="__main__":
    aadhar_number = "7720 5883 9966"
    queryAadhar(aadhar_number)