# data_preparation.py

# Import necessary libraries
import pandas as pd

# Choose or create a sample Excel spreadsheet containing relevant data
excel_file_path = "sample_data.xlsx"

# Read the Excel spreadsheet
df = pd.read_excel(excel_file_path)

# Ensure consistent structure
# For demonstration purposes, assume no specific operations are needed for consistency
if df.isnull().values.any():
    # If there are missing values, fill them with a default value or perform other handling as needed
    df.fillna(0, inplace=True)  # Fill missing values with 0 for demonstration, adjust as necessary


df.to_excel("cleaned_data.xlsx", index=False)
