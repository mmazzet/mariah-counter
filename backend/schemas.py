from pydantic import BaseModel

class EarningsResponse(BaseModel):
    today_earnings: int
    since_nov1_2025: int
    total_earnings: int