import json
import csv
import datetime

with open("../30DayQuakes.json") as DataFIle:
    data = json.load(DataFIle)

def GetSig(s):
    sig = s["properties"]["sig"]
    return 0 if sig is None else sig

significant_event = sorted(data["features"], key=GetSig, reverse=True)
significant_event = significant_event[:40]
significant_event.sort(key= lambda x: x["properties"]["time"], reverse=True)

header = ["magnitude", "place", "felt", "reports", "date", "google map link"]
row = []

for event in significant_event:
    the_date = datetime.date.fromtimestamp(
        int(event["properties"]["time"]/1000)
    )
    longitude = event["geometry"]["coordinates"][0]
    latitude = event["geometry"]["coordinates"][1]
    google_map_link = f"https://maps.google.com/maps/search/?api=1&query={latitude}%2C{longitude}"


    row.append([event["properties"]["mag"],
                event["properties"]["place"],
                0 if event["properties"]["felt"] is None else event["properties"]["felt"],
                the_date,
                google_map_link])
    
    with open ("Significant_Event.csv", "w") as CSVFile:
        writer = csv.writer(CSVFile, delimiter=",")
        writer.writerow(header)
        writer.writerows(row)