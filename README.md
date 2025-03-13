# Tech Mahindra Assignment

## Overview
This project is a Python-based data processing module that reads, processes, and validates cricket player data from different file formats (CSV & JSON). It ensures correct classification of players and 
verifies the output against expected results.

## Data Processing Workflow
1. **Read Input Data:**
   - CSV files contain player data from 1990-2000.
   - JSON files contain player data from 2000 onwards.
2. **Merge Data:**
   - Combine CSV and JSON data into a single dataset.
3. **Filter Players:**
   - Remove players with invalid ages (<15 or >50).
   - Remove players with missing 'Runs' or 'Wickets' values.
4. **Classify Players:**
   - "All-Rounder" → Runs > 500 & Wickets > 50.
   - "Batsman" → Runs > 500 & Wickets ≤ 50.
   - "Bowler" → Runs ≤ 500.
5. **Generate Output Files:**
   - Players from ODI matches are stored in `odi_result.csv`.
   - Players from Test matches are stored in `test_result.csv`.
6. **Validate Processed Data:**
   - Compare processed data with expected output datasets.
   - Mark each record as "PASS" or "FAIL" in the `Result` column.

## Files in the Repository
- `main.py` → Python script for data processing.
- `test_input_DataSet1.csv` → Sample input CSV file.
- `test_input_Dataset2.json` → Sample input JSON file.
- `test_output_dataset.csv` → Expected output dataset for Test matches.
- `od_output_dataset.csv` → Expected output dataset for ODI matches.
- `test_result.csv` → Processed results for Test matches.
- `odi_result.csv` → Processed results for ODI matches.

## How to Run the Script
1. Install dependencies (if not already installed):
   ```sh
   pip install pandas
   ```
2. Run the script:
   ```sh
   python main.py
   ```
3. Check the generated `test_result.csv` and `odi_result.csv`.

## Sample Data Processing Example
**Input (CSV/JSON):**
```csv
playerName, age, runs, wickets, eventType
JohnDoe, 30, 800, 40, TEST
JaneDoe, 29, 1200, 30, ODI
```

**Processed Output:**
```csv
playerName, age, runs, wickets, eventType, Player Type, Result
JohnDoe, 30, 800, 40, TEST, Batsman, PASS
JaneDoe, 29, 1200, 30, ODI, Batsman, PASS
```

## GitHub Submission Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/Nitin-Shelle/TechMahindra-Assignment.git
   ```
2. Make changes and commit:
   ```sh
   git add .
   git commit -m "Updated README"
   git push origin main
   ```

## Bonus Tasks (Optional Enhancements)
- **GitHub Actions**: Automate testing upon code updates.
- **Test Pipeline**: Implement unit tests using Pytest.

---
**Author:** Nitin Shelle

