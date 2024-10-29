import json
import csv

extracted_data = []

time_stamp = 1730088001

for i in range(24):
    file_name = f'TripUpdate{time_stamp}.json'
    
    print(f"{i+1}. Extracting data from: {file_name}")
    
    with open(file_name, 'r') as file:
        data = json.load(file)
        
        for entity in data.get("entity", []):
            entity_id = entity.get("id", None)
            trip_update = entity.get("trip_update", {})
            vehicle_info = trip_update.get("vehicle", {})
            vehicle_id = vehicle_info.get("id", None) if vehicle_info else None
            stop_time_updates = trip_update.get("stop_time_update", [])
            
            for stop in stop_time_updates:
                arrival_info = stop.get("arrival", {})
                departure_info = stop.get("departure", {})

                stop_id = stop.get("stop_id", None)

                if arrival_info:
                    delay = arrival_info.get("delay", None)
                    scheduled_time = arrival_info.get("schedule_time", None)
                    actual_time = arrival_info.get("time", None)
                elif departure_info:
                    delay = departure_info.get("delay", None)
                    scheduled_time = departure_info.get("schedule_time", None)
                    actual_time = departure_info.get("time", None)
                else:
                    delay = None
                    scheduled_time = None
                    actual_time = None
                
                if actual_time and time_stamp - 3600 <= actual_time < time_stamp + 3600:
                    extracted_data.append({
                        "id": entity_id,
                        "vehicle_id": vehicle_id,
                        "stop_id": stop_id,
                        "delay": delay,
                        "scheduled_time": scheduled_time,
                        "actual_time": actual_time
                    })

    print(f"Successful extraction from: {file_name}")
    
    time_stamp += 3600

csv_file = "extracted_data.csv"
fieldnames = ["id", "vehicle_id", "stop_id", "delay", "scheduled_time", "actual_time"]

with open(csv_file, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(extracted_data)

print(f"Data has been written to {csv_file}")
