# Experiment 1: Weather Dataset Download & Analysis

## Objective
To download a real-world meteorological dataset, load and inspect its structure using Pandas, perform exploratory data analysis (EDA), calculate statistical summaries, and generate visual distributions for inclusion in the machine learning laboratory record.

---

## Files in this Directory
- `weather_dataset_analysis.py`: Complete Python script for automated download, data inspection, statistics, and visualization plotting.
- `weather_dataset.csv`: Downloaded Seattle Weather dataset (automatically created upon script execution).
- `weather_visualization.png`: Exported charts (Max temperature distribution and weather condition frequency).

---

## How to Run the Program

Open PowerShell or Command Prompt in this folder and run:
```bash
python weather_dataset_analysis.py
```

---

## Expected Output Preview

```
============================================================
STEP 1: DOWNLOADING WEATHER DATASET
============================================================
SUCCESS: Dataset downloaded and saved as 'weather_dataset.csv'.

============================================================
STEP 2: LOADING AND INSPECTING DATASET
============================================================

--- Total Rows and Columns ---
Shape: 1461 rows, 6 columns

--- First 5 Records (df.head()) ---
         date  precipitation  temp_max  temp_min  wind  weather
0  2012-01-01            0.0      12.8       5.0   4.7  drizzle
1  2012-01-02           10.9      10.6       2.8   4.5     rain
2  2012-01-03            0.8      11.7       7.2   2.3     rain
3  2012-01-04           20.3      12.2       5.6   4.7     rain
4  2012-01-05            1.3       8.9       2.8   6.1     rain

--- Dataset Schema & Data Types (df.info()) ---
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1461 entries, 0 to 1460
Data columns (total 6 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   date           1461 non-null   object 
 1   precipitation  1461 non-null   float64
 2   temp_max       1461 non-null   float64
 3   temp_min       1461 non-null   float64
 4   wind           1461 non-null   float64
 5   weather        1461 non-null   object 
dtypes: float64(4), object(2)

--- Missing Values Check ---
date             0
precipitation    0
temp_max         0
temp_min         0
wind             0
weather          0
dtype: int64

--- Summary Statistics (df.describe()) ---
       precipitation  temp_max  temp_min     wind
count        1461.00   1461.00   1461.00  1461.00
mean            3.03     16.44      8.23     3.24
std             6.68      7.35      5.02     1.44
min             0.00     -1.60     -7.10     0.40
25%             0.00     10.60      4.40     2.20
50%             0.00     15.60      8.30     3.00
75%             2.80     22.20     12.20     4.00
max            55.90     35.60     18.30     9.50

============================================================
STEP 3: GENERATING DATA VISUALIZATION
============================================================
SUCCESS: Visualization plot saved as 'weather_visualization.png'.
```

---

## What to Put in Your Lab File (Screenshots)
1. **Screenshot 1:** Code editor (VS Code / PyCharm / IDLE) showing `weather_dataset_analysis.py`.
2. **Screenshot 2:** Terminal / Console output showing the successful execution and dataset statistics.
3. **Screenshot 3:** The generated visualization image `weather_visualization.png`.
