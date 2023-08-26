import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv
from os import getenv

load_dotenv()

config = {
    "host": getenv("DB_HOST"),
    "user": getenv("DB_USER"),
    "password": getenv("DB_PASSWORD"),
    "database": getenv("DB_DATABASE"),
}
# config = {
#     "host": "localhost",
#     "user": "root",
#     "password": "123456",
#     "database": "db_fastapi",
# }
print(config)


def open_database():
    def create_Table(table="user"):
        tables = {
            "user": "CREATE TABLE IF NOT EXISTS user (id int PRIMARY KEY AUTO_INCREMENT,name varchar(50),email varchar(100),age int(3))"
        }

        mydb = mysql.connector.connect(**config)
        mycursor = mydb.cursor()
        mycursor.execute(tables[table])

    try:
        mydb = mysql.connector.connect(**config)
        print("Conectou")
        create_Table()
        return mydb
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Senha errada")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            mydb = mysql.connector.connect(
                host="localhost", user="root", password="123456"
            )
            mycursor = mydb.cursor()
            mycursor.execute("CREATE DATABASE db_fastpi")
            create_Table()
            print("O banco não existia e foi criado")
