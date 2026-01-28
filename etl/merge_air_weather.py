# etl/merge_air_weather.py
import pandas as pd
from pathlib import Path
import json

# -----------------------------
# File paths
# -----------------------------
AIR_QUALITY_FILE = Path("../data /raw/air_quality/air_quality_konstanz_2026_01_01.csv")
WEATHER_FILE = Path("../data /raw/weather/weather_konstanz_2026-01-01.json")
OUTPUT_DIR = Path("../data /processed")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_FILE = OUTPUT_DIR / "merged_konstanz_2026_01_01.csv"

# -----------------------------
# Load Air Quality (semicolon CSV)
# -----------------------------
air_quality = pd.read_csv(AIR_QUALITY_FILE, sep=";")

air_quality["datetime"] = pd.to_datetime(
    air_quality["zeit"],
    errors="coerce"
)

air_quality = air_quality.sort_values("datetime")

print("Air quality loaded:")
print(air_quality.head())

## keep the updated columns only
air_quality = air_quality.drop(columns="zeit")
print("Air quality loaded updated columns:")
print(air_quality.columns)
print(air_quality.head())

# -----------------------------
# Load Weather JSON
# -----------------------------
with open(WEATHER_FILE,"r") as f:
    weather_json = json.load(f)
    print("Weather loaded:")
    print(weather_json)


weather = pd.DataFrame({
    "datetime": weather_json["hourly"]["time"],
    "temperature": weather_json["hourly"]["temperature_2m"],
    "humidity": weather_json["hourly"]["relative_humidity_2m"],
    "precipitation": weather_json["hourly"]["precipitation"]
})

weather["datetime"] = pd.to_datetime(weather["datetime"])
weather = weather.sort_values("datetime")

print("Weather loaded:")
print(weather.head())

# ------------------------
# Merge (nearest timestamp)
# ------------------------
merged = pd.merge_asof(
    air_quality,
    weather,
    on="datetime",
    direction="nearest"
)
print("Merged:")
print(merged.head())
print(merged.columns)

# ------------------------
# Save
# ----------------------
merged.to_csv(OUTPUT_FILE, index=False)
print("Merged data saved to:", OUTPUT_FILE)
print(merged.head())
print(merged['datetime'])
