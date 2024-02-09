import pandas as pd

# Read the data from the Excel spreadsheet
df = pd.read_excel("sample_data.xlsx")

# Data preprocessing steps
# Clean, filter, or aggregate the data as required
# 1. Removing duplicates
df.drop_duplicates(inplace=True)

# 2. Handling missing values
df['Sales'].fillna(df['Sales'].mean(), inplace=True)

# 3. Filtering data based on conditions
filtered_df = df[df['Sales'] > 1000]

# 4. Aggregating data
sales_by_region = df.groupby('Region')['Sales'].sum().reset_index()

# Save the processed data into a suitable format (e.g., CSV or Excel)
filtered_df.to_csv("processed_data.csv", index=False)
