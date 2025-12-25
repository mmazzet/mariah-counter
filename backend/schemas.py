from pydantic import BaseModel

class EarningsResponse(BaseModel):
    today_earnings: float
    since_nov1_2025: float
    total_earnings: float