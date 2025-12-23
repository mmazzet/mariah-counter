from fastapi import FastAPI
from calculations import calculate_earnings

app = FastAPI()

@app.get("/earnings")
async def read_earnings():
    return calculate_earnings()

