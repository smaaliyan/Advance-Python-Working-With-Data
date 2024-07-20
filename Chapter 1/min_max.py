import json

data1 = [3.0, 2.5, 5.1, 4.1, 1.8, 1.6, 2.2, 5.7, 6.1]
data2 = ['one', 'three', 'five', 'seven', 'eleven', 'eighteen']


# Finding minimum values on both data
# print(f"The minimum value in data 1 is {min(data1)}")
# print(f"The minimum value in data 2 is {min(data2, key=len)}") 


# Finding macximum values on both data                              
# print(f"The maximum value in data 1 is {max(data1)}")
# print(f"The maximum value in data 2 is {max(data2, key=len)}")

#The key=len function is used to get max and min of list of string in terms of number of letters, 
# otherwise it gets the min and max on the basis of lexagrahical order


# Try to find the max and min earthquake magnitude

with open("../30DayQuakes.json", "r") as DataFile:
    data = json.load(DataFile) 

print(data["metadata"]["title"])
print(len(data["features"]))

def getmag(dataitem):
    magnitude = dataitem["properties"]["mag"]
    if (magnitude is None):
        magnitude = 0
    return float(magnitude)

print(min(data["features"], key=getmag))
print(max(data["features"], key=getmag))
