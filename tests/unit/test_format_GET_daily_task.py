import pandas as pd

from src.daily_weather_update.tasks.format_GET_daily_api_task import (
    format_GET_daily_api,
)

raw_input = pd.read_csv("tests/fixtures/raw-weather-daily.csv")
expected_dataframe = format_GET_daily_api.fn(raw_input)


actual_dataframe = pd.read_csv("tests/fixtures/weather-daily.csv")

# format date column of expected output
actual_dataframe["date"] = pd.to_datetime(
    actual_dataframe["date"]
)  # formats datetime

# format sunrise_ux column of expected output
actual_dataframe["sunrise_ux"] = pd.to_datetime(
    actual_dataframe["sunrise_ux"], format="%Y-%m-%d"
)  # formats datetime

# format sunset_ux column of expected output
actual_dataframe["sunset_ux"] = pd.to_datetime(
    actual_dataframe["sunset_ux"], format="%Y-%m-%d"
)  # formats datetime


"""
Test task 'format_GET_daily_api' from
'format_GET_daily_api_task' with test input
compare results with expected output via. df assert
"""


def test_format_GET_daily_api():
    pd.testing.assert_frame_equal(
        expected_dataframe, actual_dataframe, check_dtype=False
    )
