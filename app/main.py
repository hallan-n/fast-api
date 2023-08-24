from fastapi import FastAPI
from .model.user import User
from .database.persistence import create_user, get_all_users

app = FastAPI()


@app.post("/")
async def set_user(user: User):
    """Set users"""
    response = create_user(user)
    if response:
        return {"response": "Create user"}
    else:
        return {"response": "Unable to create user"}


@app.get("/")
async def get_user():
    """Get users"""
    return get_all_users()
    
