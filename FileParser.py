import json

with open('TripUpdates.json', 'r') as file:
    data = json.load(file)

extracted_data = []

for entity in data.get("entity", []):
    entity_id = entity.get("id", None)
    
    trip_update = entity.get("trip_update", {})
    vehicle_info = trip_update.get("vehicle", {})
    if vehicle_info:
        vehicle_id = vehicle_info.get("id", None)
    else:
        vehicle_id = None
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
        
        extracted_data.append({
            "id": entity_id,
            "vehicle_id": vehicle_id,
            "stop_id": stop_id,
            "delay": delay,
            "scheduled_time": scheduled_time,
            "actual_time": actual_time
        })

for item in extracted_data:
    print(item)
import csv

csv_file = "extracted_data.csv"

fieldnames = ["id", "vehicle_id", "stop_id", "delay", "scheduled_time", "actual_time"]

with open(csv_file, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    
    writer.writerows(extracted_data)

print(f"Data has been written to {csv_file}")
