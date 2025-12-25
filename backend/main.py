from fastapi import FastAPI, Request
from calculations import calculate_earnings
import logging
from fastapi.middleware.cors import CORSMiddleware
from schemas import EarningsResponse

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173", "http://192.168.1.8:5173", "http://172.19.64.1:5173", "http://192.168.162.1:5173"

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

@app.get("/earnings", response_model=EarningsResponse)
async def read_earnings(request:Request):
    client_host = request.client.host
    result = calculate_earnings()
    logger.info(f"API called by IP: {client_host}, returning {result}")
    return calculate_earnings()

