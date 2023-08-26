from fastapi import FastAPI
from app.models.user import User
from app.database.persistence import (
    get_all_users,
    create_user,
    update_user,
    delete_user,
    get_user_params,
)

app = FastAPI()


@app.post("/user")
async def set_user(user: User):
    """Set users"""
    response = create_user(user)
    if response:
        return {"response": "Create user"}
    else:
        return {"response": "Unable to create user"}


@app.get("/user")
async def get_user():
    """Get users"""
    return get_all_users()


@app.get("/user/{id}")
async def get_user_for_id(id):
    """Get users"""

    return get_user_params(id)


@app.put("/user")
async def put_user(user: User):
    """Set users"""
    response = update_user(user)
    if response:
        return {"response": "Update user"}
    else:
        return {"response": "Unable to update user"}


@app.delete("/user/{id}")
async def del_user(id):
    """Set users"""
    response = delete_user(id)
    if response:
        return {"response": "Delete user"}
    else:
        return {"response": "Unable to delete user"}
