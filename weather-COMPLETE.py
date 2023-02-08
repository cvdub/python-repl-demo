#!/usr/bin/env python3

import requests
import json

API_URL = "https://api.weather.gov/"
LATITUDE = 34.4208
LONGITUDE = -119.6982


def call_api(endpoint):
    if endpoint.startswith(API_URL):
        url = endpoint
    else:
        url = API_URL + endpoint

    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.content)
    else:
        return response.status_code


def get_forecast_url(latitude, longitude):
    response = call_api(f"points/{latitude},{longitude}")
    return response["properties"]["forecast"]


def print_forecast(latitude=LATITUDE, longitude=LONGITUDE):
    url = get_forecast_url(latitude, longitude)
    forecast_data = call_api(url)

    for forecast in forecast_data["properties"]["periods"]:
        print(forecast["name"])
        print(forecast["detailedForecast"])
        print()
