import csv
from datetime import datetime

def convert_timestamp(unix_timestamp):
    if unix_timestamp:
        return datetime.fromtimestamp(int(unix_timestamp)).strftime("%I:%M:%S %p")
    return ""

def calculate_delay(scheduled, actual):
    if scheduled and actual:  
        return int(actual) - int(scheduled)
    return ""

input_csv = "extracted_data.csv"
output_csv = "extracted_data_updated.csv"

with open(input_csv, mode="r") as infile, open(output_csv, mode="w", newline="") as outfile:
    reader = csv.DictReader(infile)
    
    fieldnames = reader.fieldnames + ["scheduled_time_12hr", "actual_time_12hr", "actual_delay"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    for row in reader:
        row['scheduled_time_12hr'] = convert_timestamp(row.get('scheduled_time'))
        row['actual_time_12hr'] = convert_timestamp(row.get('actual_time'))
        row['actual_delay'] = calculate_delay(row.get('scheduled_time'), row.get('actual_time'))
        writer.writerow(row)

print(f"Timestamps have been converted, delays calculated, and saved to {output_csv}")
