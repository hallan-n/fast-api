from fastapi import APIRouter

route_user = APIRouter()


@route_user.get("/users")
def get_user():
    """Get all users"""
    return {"user": "user"}


@route_user.get("/users/{id}")
def get_user(id):
    """Get user for id"""
    return {"user": id}


@route_user.post("/users")
def set_user():
    """Set user"""
    return 200


@route_user.put("/users/{id}")
def put_user(id):
    """Put user for id"""
    return 200


@route_user.delete("/users/{id}")
def put_user(id):
    """Put user for id"""
    return 200
