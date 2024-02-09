import subprocess
import os

# Define file paths
excel_file_path = "sample_data.xlsx"
data_processing_script = "data_processing.py"

# Automation steps
# Open Excel
subprocess.Popen(["start", excel_file_path], shell=True)

# Wait for Excel to open (add appropriate waiting time if necessary)
# This sleep command is just a placeholder and might need adjustment based on system performance
import time
time.sleep(5)

# Run the data processing script
subprocess.Popen(["python", data_processing_script], shell=True)

# Wait for the data processing script to complete (add appropriate waiting time if necessary)
# This sleep command is just a placeholder and might need adjustment based on the processing time
time.sleep(10)

# Check if the processed data file exists
processed_data_file = "processed_data.csv"
if os.path.exists(processed_data_file):
    print("Data processing completed successfully.")
    print(f"Processed data saved as: {processed_data_file}")
else:
    print("Error: Processed data file not found.")

# Open Excel, run Python script, save processed data
subprocess.run(["start", "excel.exe", "sample_data.xlsx"])
subprocess.run(["python", "data_processing.py"])
