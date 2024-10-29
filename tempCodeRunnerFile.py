with open(input_csv, mode="r") as infile, open(output_csv, mode="w", newline="") as outfile:
#     reader = csv.DictReader(infile)
    
#     fieldnames = reader.fieldnames + ["scheduled_time_12hr", "actual_time_12hr", "actual_delay"]
#     writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    
#     writer.writeheader()
    
#     for row in reader:
#         row['scheduled_time_12hr'] = convert_timestamp(row.get('scheduled_time'))
#         row['actual_time_12hr'] = convert_timestamp(row.get('actual_time'))
#         row['actual_delay'] = calculate_delay(row.get('scheduled_time'), row.get('actual_time'))
#         writer.writerow(row)