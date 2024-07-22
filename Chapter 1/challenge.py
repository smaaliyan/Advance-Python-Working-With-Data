import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)
    
def AreQuakes(q):
    if (q["properties"]["type"] == "earthquake"):
        return True
    return False

    
def Felt100Quakes(q):
    return sum(
        quake["properties"]["felt"] is not None and quake["properties"]["felt"] >= 100
        for quake in q["features"]
    )

print(Felt100Quakes(data))










are_quake = list(filter(AreQuakes, data["features"]))
# print(f"The number of quakes that are felt are {len(are_quake)}")