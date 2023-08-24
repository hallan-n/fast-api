from .connection import open_database
from ..model.user import User


def create_user(user: User) -> bool:
    """Insert user"""

    mydb = open_database()
    mycursor = mydb.cursor()
    query = f"INSERT INTO user (name,email,age) VALUES ('{user.name}','{user.email}',{user.age})"
    mycursor.execute(query)
    mydb.commit()
    mydb.close()
    return True

def get_all_users() -> list[User]:
    """Get all user"""

    mydb = open_database()
    mycursor = mydb.cursor()
    query = "SELECT * FROM user"
    mycursor.execute(query)
    result = mycursor.fetchall()
    users = []
    for x in result:
        user = {
            "id": x[0],
            "name": x[1],
            "email": x[2],
            "age": x[3]
        }
        users.append(user)
    return users

