import pandas as pd
import os

# Create output folder if not exists
os.makedirs("output", exist_ok=True)

# Load the master Excel file
df = pd.read_excel("sample_data/master.xlsx")

# Basic transformation: clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Example: split by 'region'
if 'region' not in df.columns:
    raise Exception("Column 'region' is required in the input file.")

for region, group in df.groupby('region'):
    # Example transformations:
    group = group.drop(columns=["internal_notes"], errors='ignore')
    group = group.sort_values(by="client_name")

    # Add a calculated column
    if "amount" in group.columns and "quantity" in group.columns:
        group["total"] = group["amount"] * group["quantity"]

    # Export to Excel
    filename = f"output/{region}.xlsx"
    group.to_excel(filename, index=False)

print("✅ Split and export completed.")
