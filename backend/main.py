from fastapi import FastAPI, Request
from calculations import calculate_earnings
import logging

app = FastAPI()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

@app.get("/earnings")
async def read_earnings(request:Request):
    client_host = request.client.host
    logger.info(f"API called by IP: {client_host}")
    return calculate_earnings()

