from datetime import datetime, date
import logging

START_DATE_2025 = date(2025, 11, 1)
TOTAL_EARNINGS_SINCE_1994 = 100_000_000
EARNINGS_PER_DAY = 8200

logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def get_days_since(start_date: date, current_time: datetime) -> int:
    """
    Returns the number of full days between start_date and current_time.
    """
    difference = current_time.date() - start_date
    return max(difference.days, 0)  # avoid negative values


def compute_today_earnings(earnings_per_day: int) -> int:
    """
    Returns today's earnings.
    """
    return earnings_per_day


def calculate_since_nov_2025(days_since_start: int, earnings_per_day: int) -> int:
    """
    Calculates earnings since Nov 1, 2025.
    """
    return days_since_start * earnings_per_day


# -------------------------
# Main function
# -------------------------

def calculate_earnings(current_time: datetime | None = None) -> dict:
    if current_time is None:
        current_time = datetime.now()

    logger.info(f"Calculating earnings at {current_time}")

    days_since_nov2025 = get_days_since(START_DATE_2025, current_time)

    logger.info(f"Days since 1st Nov 2025: {days_since_nov2025}")

    earnings_since_nov2025 = calculate_since_nov_2025(
        days_since_nov2025,
        EARNINGS_PER_DAY
    )
    today_earnings = compute_today_earnings(EARNINGS_PER_DAY)
    total_earnings = TOTAL_EARNINGS_SINCE_1994 + earnings_since_nov2025

    logger.info(f"Today earnings: {today_earnings}, Total earnings: {total_earnings}")


    return {
        "today_earnings": today_earnings,
        "since_nov1_2025": earnings_since_nov2025,
        "total_earnings": total_earnings,
    }

if __name__ == "__main__":
    result = calculate_earnings()
    print(result)