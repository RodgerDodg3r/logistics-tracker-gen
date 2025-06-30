# Loading Plan Tracker Generator

📋 A simple and powerful Python script that parses a loading plan from a CSV file and generates a tracker-friendly output as `tracker.csv`.

## ❗Applying Python to a Real-World Logistics Challenge

Creating a daily loading tracker was a repetitive and time-consuming task that typically took between 30 to 40 minutes each day. The process involved manually extracting data from spreadsheets, organizing it by vehicle loads, and formatting it into a structured summary for logistics tracking. This not only consumed valuable time but also introduced the risk of human error. Recognizing this inefficiency, I saw an opportunity to apply my programming skills to streamline the workflow. I developed a Python script that automates the entire process — reading raw data from CSV files, organizing it into structured load records, and generating a ready-to-use tracker file in seconds. This solution significantly improved productivity, reduced errors, and demonstrated my ability to solve real-world problems through automation.


## 🔧 Features

- Extracts vehicle loads and depot details from structured loading plan files
- Aggregates departure times, hauliers, and pallet counts
- Avoids duplicate depot entries per vehicle
- Outputs a clean CSV report suitable for tracking or logistics review

## 🔐Security 

Security and data integrity were key considerations in developing this tracker automation tool. Since the data includes sensitive logistics information such as vehicle numbers, departure times, and depot details, I ensured that the script operates strictly on local files with no external dependencies or network access. This minimizes exposure and keeps all information within a secure environment. Additionally, by eliminating the need for manual handling and repetitive copy-pasting, the risk of accidental data leakage or misentry is significantly reduced. The code also avoids storing any data beyond the runtime of the script, ensuring that no sensitive information is persistently cached or logged. This approach reflects my awareness of secure development practices, especially when dealing with operational data.


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
