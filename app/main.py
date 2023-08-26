from fastapi import FastAPI
from app.models.user import User
from app.database.persistence import get_all_users, create_user

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
