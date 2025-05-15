from fastapi import FastAPI
from .db.connection import get_connection  # Using relative import

app = FastAPI()

@app.get("/")
async def root():
    conn = get_connection()
    if conn:
        conn.close()  # Close the connection after testing
        return {"message": "Database connection successful"}
    else:
        return {"message": "Failed to connect to the database"}
