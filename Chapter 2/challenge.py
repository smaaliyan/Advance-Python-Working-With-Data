import json
from collections import defaultdict, Counter

with open('../30DayQuakes.json', 'r') as DataFile:
    data = json.load(DataFile)

# use a defaultdict to categorize each event and count each one
totals = defaultdict(int)
for event in data['features']:
    totals[event['properties']['type']] += 1

for k, v in totals.items():
    print(f"{k:15}: {v}")
