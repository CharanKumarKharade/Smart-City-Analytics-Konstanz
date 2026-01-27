# etl/extract_weather_konstanz.py

import requests
import json
from pathlib import Path
from datetime import datetime
import sys

# -----------------------------
# Config
# -----------------------------
LATITUDE = 47.6779
LONGITUDE = 9.1750
CITY = "konstanz"
DATE = "2026-01-01"

BASE_URL = "https://api.open-meteo.com/v1/forecast"
PARAMS = {
    "latitude": LATITUDE,
    "longitude": LONGITUDE,
    "hourly": "temperature_2m,relative_humidity_2m,precipitation",
    "timezone": "Europe/Berlin"
}

# -----------------------------
# Output path
# -----------------------------
output_dir = Path("../data /raw/weather")
output_dir.mkdir(parents=True, exist_ok=True)
output_file = output_dir / f"weather_{CITY}_{DATE}.json"

# -----------------------------
# Fetch weather
# -----------------------------
try:
    response = requests.get(BASE_URL, params=PARAMS, timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error fetching weather data: {e}")
    sys.exit(1)

weather_data = response.json()

# -----------------------------
# Save JSON
# -----------------------------
with open(output_file, "w") as f:
    json.dump(weather_data, f, indent=2)

print(f"Weather data saved successfully: {output_file}")
