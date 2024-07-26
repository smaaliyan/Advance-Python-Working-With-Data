import json
import datetime

with open("../30DayQuakes.json", "r") as DataFile:
    data = json.load(DataFile)

# Since the data is too bif I am taking only those data whose magnitude are greater than 5
def IsBig(x):
    mag = x["properties"]["mag"]
    return mag is not None and mag > 6

larger_quakes = list(filter(IsBig, data["features"]))

# defineing a functuon to make the JSON file simpler
def simpleJson(j):
    return{
        "place": j["properties"]["place"],
        "mag": j["properties"]["mag"],
        "url": j["properties"]["url"],
        "date": str(datetime.date.fromtimestamp(int(j["properties"]["time"])/1000))
    }


# Transform the data to a JSON format we want to save
larger_quakes = list(map(simpleJson, larger_quakes))

# Usind dump() function to write json to a string
string = json.dumps(larger_quakes, sort_keys=True, indent=4)
print(string)

# Using dump() function to write JSON to a file
with open("larger_Quakes.json", "w") as JsonFile:
    json.dump(larger_quakes, JsonFile, sort_keys=True, indent=4)