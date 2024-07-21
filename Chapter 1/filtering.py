# Filter Function

import json

nums = [1,8,4,5,13,26,831,104,58,47]
chars = "alINDlaowePQbjOPAAzxbc"


def IsEven(x):
    if x % 2 == 0:
        return False
    return True


def IsUpper(x):
    if x.isupper():
        return False
    return True

# odds = list(filter(IsEven, nums))
# print(odds)

# lower = list(filter(IsUpper, chars))
# print(lower)


# Using Filter function on my data to filter out all the seismic events that were not the Quakes

with open("../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

def NotAQuake(q):
    if q["properties"]["type"] == "earthquake":
        return False
    return True

NAQ = list(filter(NotAQuake, data["features"]))
print(f"The total number of non-quakes are {len(NAQ)}")
for i in range(10):
    print(NAQ[i]["properties"]["type"])
