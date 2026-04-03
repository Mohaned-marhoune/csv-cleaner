# CSV Cleaner 🧹

A simple Python script that cleans messy CSV files automatically.

## What it does

- Removes duplicate rows
- Fills missing values with smart defaults
- Standardizes name formatting (Title Case)
- Normalizes email addresses (lowercase)
- Exports a clean CSV file ready to use

## Requirements

- Python 3.x
- pandas

## Installation
```bash
pip install pandas
```

## Usage
```bash
python3 cleaner.py
```

## Input vs Output

| Before | After |
|---|---|
| Duplicate rows | Removed |
| Empty names | Filled with "Unknown" |
| Missing numbers | Filled with median value |
| Mixed case emails | Normalized to lowercase |

## Output

The cleaned file is saved automatically as `cleaned_output.csv`

## Author

Mohaned Marhoune — Open for freelance work
[GitHub](https://github.com/Mohaned-marhoune)
