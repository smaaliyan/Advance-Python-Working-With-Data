import json

# data = [0,1,2,3,4,5]

# any() function used to check if any value in the dataset is TRUE, (0=FALSE, Other than 0 is TRUE)
# print(any(data))


# all() function is used to if all the values in the dataset is TRUE, (0=FALSE, Other than 0 is TRUE)
# print(all(data))

# sum() function is used to add all of the values in the sequence in the dataset
# print(sum(data))


with open("../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Check is there any Earthquake that were felt by more than 25000 peoples
print(any(quake["properties"]["felt"] is not None and quake["properties"]["felt"] > 25000
          for quake in data["features"]))

# Calculate how many earthquakes are felt by more than 500 peoples
print(sum(quake["properties"]["felt"] is not None and quake["properties"]["felt"] > 500
          for quake in data["features"]))

# Calculating how many earthquakes had a magnitude of 6 or larger
print(sum(quake["properties"]["mag"] is not None and quake["properties"]["mag"] >= 6
          for quake in data["features"]))



