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
- **Location:** `data/raw/air_quality/air_quality_konstanz_2026_01_01.csv`

### Weather Data — Konstanz
- **Source:** Open-Meteo API
- **Metrics:** Temperature, Relative Humidity, Precipitation
- **Granularity:** Hourly
- **Coverage:** 1 Jan → 2 Feb 2026
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
- ✅ Commit: `feat: Initial air quality data load for 1 Jan 2026`

### Day 2
- Extracted **weather data** for Konstanz from 1 Jan → 2 Feb 2026 using Open-Meteo API
- Saved raw JSON files in `data/raw/weather/`
- Updated README with weather dataset info
- ✅ Commit: `feat: Extract weather data for Konstanz 1 Jan → 2 Feb 2026`

---

## Next Steps
- **Day 3:** Merge **air quality (1 Jan)** with weather data for the same day  
- **Day 4:** Clean and align merged data, handle missing values, prepare for analysis  
- Compare 1 Jan air quality against **weather trends from 1 Jan → 2 Feb 2026**  
- Extend to additional days if needed to strengthen insights
