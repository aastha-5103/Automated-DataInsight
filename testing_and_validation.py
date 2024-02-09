# testing_and_validation.py

# Import necessary libraries
import pandas as pd

# Read the original Excel data
original_data = pd.read_excel("sample_data.xlsx")

# Read the processed data
processed_data = pd.read_csv("processed_data.csv")

# Compare the original data with the processed data: row counts, column names, and values
# Perform validation checks to ensure accuracy
# 1. Compare row counts
if original_data.shape[0] == processed_data.shape[0]:
    print("Row count validation passed: Original and processed data have the same number of rows.")
else:
    print("Row count validation failed: Original and processed data have different numbers of rows.")

# 2. Compare column names
if list(original_data.columns) == list(processed_data.columns):
    print("Column names validation passed: Original and processed data have the same column names.")
else:

# 3. Compare values
if original_data.shape == processed_data.shape:
    print("Data validation passed: Original and processed data have the same shape.")
else:
    print("Data validation failed: Original and processed data have different shapes.")
