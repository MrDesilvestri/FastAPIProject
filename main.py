from fastapi import FastAPI
from decouple import config
import pymysql

app = FastAPI()
DB_connection = pymysql.connect(host = config('DB_HOST'), user = config('DB_USER'), password = config('DB_PASSWORD'), db = config('DB_NAME'), port=int(config('DB_PORT', default=3306)))
cur = DB_connection.cursor()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/usersMariaDB")
def read_users():
    cur.execute("SELECT * FROM Persona")
    return cur.fetchall()
@app.get("/usersMongoDB")
def read_users():
    return {"message": "In Progress!!"}