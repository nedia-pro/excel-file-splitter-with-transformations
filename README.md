# Excel File Splitter with Transformations

This Python script reads a master Excel file, performs data cleaning and transformations, and splits the content into multiple Excel files based on the 'Region' column.

## Features

- Automatically splits the data by region
- Cleans column names and drops unnecessary columns
- Adds a calculated column: `Total = Amount * Quantity`
- Saves output files in a structured folder

## How to Use

1. Place your `master.xlsx` inside the `sample_data/` folder.
2. Run the script:
   ```bash
   python splitter.py
   ```
3. Find your result files in the `output/` folder.

## Technologies Used

- Python 3
- pandas
- openpyxl

---

