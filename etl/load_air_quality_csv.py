# etl/load_air_quality.py

import pandas as pd
from pathlib import Path
import sys

# -----------------------------
# File path
# -----------------------------
AQ_FILE = Path("../data /raw/air_quality/air_quality_konstanz_2026_01_01.csv")

# Check if the file exists
if not AQ_FILE.is_file():
    print(f"Error: Air quality file not found at {AQ_FILE}")
    sys.exit(1)

# -----------------------------
# Load CSV
# -----------------------------
try:
    df = pd.read_csv(AQ_FILE)
except Exception as e:
    print(f"Error loading CSV: {e}")
    sys.exit(1)

# -----------------------------
# Standardize datetime
# -----------------------------
if 'datetime' in df.columns:
    df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')
else:
    print("Warning: 'datetime' column not found in CSV")

# -----------------------------
# Quick inspection
# -----------------------------
print("Columns:", df.columns.tolist())
print("First 5 rows:\n", df.head())
print("Missing values:\n", df.isnull().sum())
print(f"Loaded {len(df)} rows from {AQ_FILE}")
