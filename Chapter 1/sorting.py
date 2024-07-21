import json

numbers = [43,65,32,75,98,34,12]
names = ['Aaliyan', "Owais", "Rayyan", "Shafiq", "Hammad", "Shumaim", "Hamza", "Waqar"]


# The sorted() function can be used to return a new list with sorted elements, doesn't touch the orignal data
# result1 = sorted(numbers)
# result2 = sorted(names)
# print(result1)
# print(result2)

# The sort() method makes the changes (do Sorting) into the orignal data
# numbers.sort(reverse=True)
# print(numbers)

# names.sort(reverse=True)
# print(names)


# Printing top 10 places where the earthquake magnitude is high
with open("../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

def getmag(dataitem):
    magnitude = dataitem["properties"]["mag"]
    if (magnitude is None):
        magnitude = 0
    return float(magnitude)

data["features"].sort(key=getmag, reverse=True)

for i in range(10):
    print(data["features"][i]["properties"]["place"])