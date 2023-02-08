#!/usr/bin/env python3

import requests
import json

LATITUDE = 34.4208
LONGITUDE = -119.6982


def call_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.content)
    else:
        return response.status_code


def get_forecast_url(latitude, longitude):
    call_api(f"https://api.weather.gov/points/{latitude},{longitude}")
    return response["properties"]["forecast"]


def print_forecast(latitude=LATITUDE, longitude=LONGITUDE):
    url = get_forecast_url(latitude, longitude)
    forecast_data = call_api(url)
    for period in forecast_data["properties"]["periods"]:
        print(period["name"] + ":")
        print(period["detailedForecast"])
        print()
