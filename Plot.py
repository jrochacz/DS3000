import csv
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

def timestamp_to_hour(timestamp):
    if timestamp:
        time_obj = datetime.fromtimestamp(int(timestamp))
        return time_obj.hour + time_obj.minute / 60 + time_obj.second / 3600  
    return None

csv_file = "extracted_data_updated.csv"
hours = []
delays_minutes = []

with open(csv_file, mode="r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        actual_time = row.get("actual_time")
        actual_delay = row.get("actual_delay")
        
        if actual_time and actual_delay:
            hours.append(timestamp_to_hour(actual_time))
            delays_minutes.append(int(actual_delay) / 60)  

plt.style.use('dark_background')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Scatter plot
ax1.scatter(hours, delays_minutes, label='Actual Delay', alpha=0.2, color='cyan')
ax1.set_title("Actual Delay Over Time", fontsize=16, fontweight='bold', color='white')
ax1.set_xlabel("Actual Time (Hours)", fontsize=14, color='white')
ax1.set_ylabel("Actual Delay (Minutes)", fontsize=14, color='white')
ax1.set_xlim(0, 24)  
ax1.set_xticks(range(0, 25, 1)) 
ax1.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)  
ax1.legend(fontsize=12, loc='upper left', frameon=True)

# Histogram 
ax2.hist(delays_minutes, bins=50, alpha=0.7, color='orange')
ax2.set_title("Histogram of Actual Delays", fontsize=16, fontweight='bold', color='white')
ax2.set_xlabel("Delay (Minutes)", fontsize=14, color='white')
ax2.set_ylabel("Frequency", fontsize=14, color='white')
ax2.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)  

# Pie chart
fig_pie, ax3 = plt.subplots(figsize=(8, 8))
bins = np.arange(0, max(delays_minutes) + 10, 10)
delay_categories = np.histogram(delays_minutes, bins=bins)[0]
delay_labels = [f"{i}-{i + 10}" for i in bins[:-1]]

threshold = 1
display_labels = [label if count > threshold else "" for label, count in zip(delay_labels, delay_categories)]

explode = [0.1] * len(delay_categories)  

ax3.pie(delay_categories, 
         labels=display_labels, 
         autopct=lambda p: f'{p:.1f}%' if p > threshold else '',  
         startangle=90, 
         colors=plt.cm.Paired.colors, 
         explode=explode,
         shadow=True) 

ax3.axis('equal')  
ax3.set_title("Percentage of Delays by 10-Minute Intervals", fontsize=16, fontweight='bold', color='white')

fig_pie.patch.set_facecolor('#212121')  

plt.tight_layout()
plt.show()
