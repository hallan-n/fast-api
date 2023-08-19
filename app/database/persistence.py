from connection import close_database, open_database
from model.user import User


def create_user(user: User):
    """Insert user"""
    mydb = open_database()
    mycursor = mydb.cursor()
    query = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    value = ("John", "Highway 21")
    mycursor.execute(query, value)
    mydb.commit()
    close_database()
    return True

def get_user():
    """Get all users"""
    return {"user": "user"}


def get_user(id):
    """Get user for id"""
    return {"user": id}


def set_user():
    """Set user"""
    return 200


def put_user(id):
    """Put user for id"""
    return 200


def put_user(id):
    """Put user for id"""
    return 200
