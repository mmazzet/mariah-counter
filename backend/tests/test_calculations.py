from datetime import datetime, date
from calculations import get_days_since, calculate_since_nov_2025, EARNINGS_PER_DAY, calculate_earnings, TOTAL_EARNINGS_SINCE_1994

def test_get_days_since():
  start_date = date(2025, 11, 1)
  current_time = datetime(2025, 11, 3, 12, 0, 0)

  days = get_days_since(start_date, current_time)

  assert days == 2

def test_get_days_since_before_start():
  start_date = date(2025, 11, 1)
  current_time = datetime(2025, 10, 30, 12, 0, 0)

  days = get_days_since(start_date, current_time)

  assert days == 0

def test_calculate_since_nov_2025_basic():
  days = 2
  total = calculate_since_nov_2025(days, EARNINGS_PER_DAY)
  assert total == 2 * EARNINGS_PER_DAY

def test_calculate_since_nov_2025_zero_days():
  days = 0
  total = calculate_since_nov_2025(days, EARNINGS_PER_DAY)
  assert total == 0 * EARNINGS_PER_DAY

def test_calculate_earnings_normal():
  current_time = datetime(2025, 11, 3, 12, 0, 0)
  result = calculate_earnings(current_time)

  expected_since_nov1 = 2 * EARNINGS_PER_DAY
  expected_total = TOTAL_EARNINGS_SINCE_1994 + expected_since_nov1

  assert result["today_earnings"] == EARNINGS_PER_DAY
  assert result["since_nov1_2025"] == expected_since_nov1
  assert result["total_earnings"] == expected_total

def test_calculate_earnings_before_start():
  current_time = datetime(2025, 10, 30, 12, 0, 0)
  result = calculate_earnings(current_time)

  assert result["today_earnings"] == EARNINGS_PER_DAY
  assert result["since_nov1_2025"] == 0
  assert result["total_earnings"] == TOTAL_EARNINGS_SINCE_1994
