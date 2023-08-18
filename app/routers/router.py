from database import connection, persistence
from fastapi import FastAPI


app = FastAPI()

@app.get("/{value}")
async def root(value: str):
    try:
        parse = int(value)
        connection.open_database()
        return {"message": f"{parse} é inteiro"}
    except:
        return {"message": f"{value} é um texto"}
    


