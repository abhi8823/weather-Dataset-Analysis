"""
Experiment 1: Weather Dataset Download, Preprocessing, and Exploration
Description:
    Downloads a real-world weather dataset (Seattle Weather Dataset),
    loads it into a Pandas DataFrame, performs exploratory data analysis (EDA),
    checks for missing values, computes descriptive statistics, and saves
    visualizations for lab reporting.
"""

import os
import urllib.request
import pandas as pd
import matplotlib.pyplot as plt

DATASET_URL = "https://raw.githubusercontent.com/vega/vega-datasets/master/data/seattle-weather.csv"
DATASET_FILE = "weather_dataset.csv"
PLOT_FILE = "weather_visualization.png"

def download_dataset():
    print("=" * 60)
    print("STEP 1: DOWNLOADING WEATHER DATASET")
    print("=" * 60)
    if os.path.exists(DATASET_FILE):
        print(f"Dataset already exists locally: '{DATASET_FILE}'. Skipping download.")
        return

    print(f"Fetching dataset from URL:\n  {DATASET_URL}")
    try:
        urllib.request.urlretrieve(DATASET_URL, DATASET_FILE)
        print(f"SUCCESS: Dataset downloaded and saved as '{DATASET_FILE}'.")
    except Exception as e:
        print(f"Network download failed: {e}")
        print("Creating local fallback sample dataset...")
        sample_data = {
            "date": ["2012-01-01", "2012-01-02", "2012-01-03", "2012-01-04", "2012-01-05"],
            "precipitation": [0.0, 10.9, 0.8, 20.3, 1.3],
            "temp_max": [12.8, 10.6, 11.7, 12.2, 8.9],
            "temp_min": [5.0, 2.8, 7.2, 5.6, 2.8],
            "wind": [4.7, 4.5, 2.3, 4.7, 6.1],
            "weather": ["drizzle", "rain", "rain", "rain", "rain"]
        }
        pd.DataFrame(sample_data).to_csv(DATASET_FILE, index=False)
        print(f"Fallback dataset saved to '{DATASET_FILE}'.")

def analyze_dataset():
    print("\n" + "=" * 60)
    print("STEP 2: LOADING AND INSPECTING DATASET")
    print("=" * 60)
    df = pd.read_csv(DATASET_FILE)
    
    print(f"\n--- Total Rows and Columns ---")
    print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")

    print(f"\n--- First 5 Records (df.head()) ---")
    print(df.head())

    print(f"\n--- Dataset Schema & Data Types (df.info()) ---")
    df.info()

    print(f"\n--- Missing Values Check ---")
    missing = df.isnull().sum()
    print(missing)

    print(f"\n--- Summary Statistics (df.describe()) ---")
    print(df.describe().round(2))

    if "weather" in df.columns:
        print(f"\n--- Weather Condition Frequency Distribution ---")
        print(df["weather"].value_counts())

    # Generate Visualization for lab report
    print("\n" + "=" * 60)
    print("STEP 3: GENERATING DATA VISUALIZATION")
    print("=" * 60)
    try:
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))

        # Subplot 1: Histogram of Max Temperature
        axes[0].hist(df["temp_max"], bins=25, color="skyblue", edgecolor="black")
        axes[0].set_title("Distribution of Maximum Temperature (°C)")
        axes[0].set_xlabel("Max Temperature (°C)")
        axes[0].set_ylabel("Frequency")
        axes[0].grid(True, linestyle="--", alpha=0.6)

        # Subplot 2: Weather Condition Counts
        if "weather" in df.columns:
            counts = df["weather"].value_counts()
            axes[1].bar(counts.index, counts.values, color="coral", edgecolor="black")
            axes[1].set_title("Count of Weather Types")
            axes[1].set_xlabel("Weather Condition")
            axes[1].set_ylabel("Occurrences")
            axes[1].tick_params(axis='x', rotation=30)
            axes[1].grid(axis="y", linestyle="--", alpha=0.6)

        plt.tight_layout()
        plt.savefig(PLOT_FILE, dpi=200)
        print(f"SUCCESS: Visualization plot saved as '{PLOT_FILE}'.")
        print("You can view or include this plot in your lab file!")
    except Exception as ex:
        print(f"Could not generate plot: {ex}")

    print("\n" + "=" * 60)
    print("PROGRAM COMPLETED SUCCESSFULLY!")
    print("=" * 60)

if __name__ == "__main__":
    download_dataset()
    analyze_dataset()
