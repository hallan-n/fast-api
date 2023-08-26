from app.database.connection import open_database
from app.models.user import User


def create_user(user: User) -> bool:
    """Insert user"""

    mydb = open_database()
    mycursor = mydb.cursor()
    query = f"INSERT INTO user (name,email,age) VALUES ('{user.name}','{user.email}',{user.age})"
    mycursor.execute(query)
    mydb.commit()
    mydb.close()
    return True


def get_all_users():
    """Get all user"""

    mydb = open_database()
    mycursor = mydb.cursor()
    query = "SELECT * FROM user"
    mycursor.execute(query)
    result = mycursor.fetchall()
    users = []
    for x in result:
        user = {"id": x[0], "name": x[1], "email": x[2], "age": x[3]}
        users.append(user)
    print(result)
    return users

def get_user_params(id):
    """Get all user"""

    mydb = open_database()
    mycursor = mydb.cursor()
    query = f"SELECT * FROM db_fastapi.user WHERE id={id}"
    mycursor.execute(query)
    result = mycursor.fetchone()
    return result


def update_user(user: User):
    """Get all user"""

    mydb = open_database()
    mycursor = mydb.cursor()
    query = f"UPDATE user SET name='{user.name}', email='{user.email}', age={user.age} WHERE id = {user.id};"
    mycursor.execute(query)
    mydb.commit()
    mydb.close()
    return True


def delete_user(id):
    """Get all user"""

    mydb = open_database()
    mycursor = mydb.cursor()
    query = f"DELETE FROM user WHERE id={id}"
    mycursor.execute(query)
    mydb.commit()
    mydb.close()
    return True
