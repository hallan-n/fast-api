import mysql.connector
from mysql.connector import errorcode


config = {
    "host": "localhost",
    "user": "root",
    "password": "123456",
    "database": "db_fastpi",
}


def open_database():
    try:
        mydb = mysql.connector.connect(**config)
        print("Conectou")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Senha errada")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            mydb = mysql.connector.connect(
                host="localhost", user="root", password="123456"
            )
            mycursor = mydb.cursor()
            mycursor.execute("CREATE DATABASE db_fastpi")
            print("O banco não existia e foi criado")


def close_database():
    mydb = mysql.connector.connect(**config)
    mydb.close()
