# Smart City Analytics — Konstanz 2026

## Project Overview
This project analyzes environmental conditions in Konstanz by combining **air quality** and **weather** data.  
The goal is to understand hourly patterns, correlations between weather and pollutants, and highlight deviations on **1 Jan 2026**.  
This project demonstrates an **end-to-end data analyst workflow**: ETL → Cleaning → Integration → Analysis → Insights.

---

## Data Sources

### Air Quality Data — Konstanz
- **Source:** German Environment Agency (UBA)
- **Metrics:** PM2.5, PM10, NO₂
- **Granularity:** Hourly
- **Coverage:** 1 Jan 2026 (single day)
- **Data type:** CSV (semicolon-separated `;`)
- **Location:** `data/raw/air_quality/air_quality_konstanz_2026_01_01.csv`

### Weather Data — Konstanz
- **Source:** Open-Meteo API
- **Metrics:** Temperature, Relative Humidity, Precipitation
- **Granularity:** Hourly
- **Coverage:** 1 Jan → 2 Feb 2026
- **Data type:** JSON (hourly observations)
- **Location:** `data/raw/weather/`

---

## ETL Progress

### Day 1
- Project folders created:
  - `data/raw/air_quality/`  
  - `data/raw/weather/`  
  - `data/processed/`  
  - `etl/`  
- Loaded **air quality CSV** for 1 Jan 2026
- Standardized `datetime` column
- Verified columns and missing values


### Day 2
- Extracted **weather data** for Konstanz from 1 Jan → 2 Feb 2026 using Open-Meteo API
- Saved raw JSON files in `data/raw/weather/`
- Updated README with weather dataset info


### Day 3
- Merged air quality and weather datasets for 1 Jan 2026 using pandas.merge_asof 
- Ensures each air quality measurement is aligned with the nearest weather observation as of that time 
- Handles non-aligned timestamps between sensors and API data 
- Cleaned merged dataset: kept columns entry_id, datetime, o3, no2, pm10, pm25, temperature, humidity, precipitation 
- Saved processed CSV in `data/processed/merged_konstanz_2026_01_01.csv `
- Updated README with ETL + merge logic, explaining merge_asof usage


### Day 4
- Verified row count and column consistency
- Checked missing values after time-based merge
- Ensured pollutant and weather ranges are realistic
- Prepared cleaned dataset for analysis


---
## Next Steps
- **Day 5:** Preview 
- Visualize hourly PM trends
- Compare PM vs temperature 
- Correlation matrix

