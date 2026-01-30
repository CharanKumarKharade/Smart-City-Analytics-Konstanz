import pandas as pd

merged = pd.read_csv("../data /processed/merged_konstanz_2026_01_01.csv",
                     parse_dates=["datetime"])
print(merged.describe())
print(merged.shape)
cleaned = merged.dropna(
    subset=["pm25", "pm10", "no2", "o3"],
    how="all"
)
cleaned.to_csv("../data /processed/merged_konstanz_2026_01_01_clean.csv",
    index=False)

print("Cleaned Dataset saved")