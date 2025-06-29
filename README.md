# Loading Plan Tracker Generator

📋 A simple and powerful Python script that parses a loading plan from a CSV file and generates a tracker-friendly output as `tracker.csv`.

## 🔧 Features

- Extracts vehicle loads and depot details from structured loading plan files
- Aggregates departure times, hauliers, and pallet counts
- Avoids duplicate depot entries per vehicle
- Outputs a clean CSV report suitable for tracking or logistics review

## 🛠️ Requirements

- Python 3.x
- Standard library only (no external dependencies)

## 📁 Input Format

The input CSV file (`load_plan.csv`) should contain headers like:

- `Vehicle No.`
- `Customer Depot`
- `Time of Departure`
- `Haulier`
- `MORAN` (used for pallet count)

**Note:** The script looks for these headers and assumes `TOTAL` marks the row where pallet numbers are provided.

## 🚀 Usage

1. Place your `load_plan.csv` file in the project directory.
2. Run the script:

```bash
python main.py
