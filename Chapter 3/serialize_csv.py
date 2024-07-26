import csv
import json
import datetime

with open("../30DayQuakes.json", "r") as DataFile:
    data = json.load(DataFile)

# Since the data is too bif I am taking only those data whose magnitude are greater than 5
def IsBig(x):
    mag = x["properties"]["mag"]
    return mag is not None and mag > 5

larger_quakes = list(filter(IsBig, data["features"]))

# First create a header and row structure for the data
header = ["Place", "Magnitude", "Link", "Date"]
row = []

# Now populate the rows with with resulting data
for quake in larger_quakes:
    thedate = datetime.date.fromtimestamp(
        int(quake["properties"]["time"]/1000)
        )
    
    row.append([quake["properties"]["place"],
               quake["properties"]["mag"],
               quake["properties"]["url"],
               thedate])
    
# Writing the file to the CSV file
with open("larger_Quake.csv", "w") as CSVFile:
    writer = csv.writer(CSVFile, delimiter=",")
    writer.writerow(header)
    writer.writerows(row)

