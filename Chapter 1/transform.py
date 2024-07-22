import json
import datetime
import pprint

nums = [1, 8, 4, 5, 31, 62, 183, 104, 85, 47]
grades = [81, 89, 94, 78, 61, 66, 99, 74]

def SquareFunc(x):
    return x**2

def GradeFunc(x):
    if (x >= 90):
        return "A"
    elif (x >= 80):
        return "B"
    elif (x >= 70):
        return "C"
    elif (x >= 60):
        return "D"
    return "F"

# map() function applies the function to the all the iterator

# square = list(map(SquareFunc, nums))
# print(square)

# grade = list(map(GradeFunc, grades))
# print(grade)

with open("../30DayQuakes.json", "r") as DataFile:
    data = json.load(DataFile)

# filtering down the data to the largest events
def bigMag(x):
    return x["properties"]["mag"] is not None and x["properties"]["mag"] >= 6

result = list(filter(bigMag, data["features"]))
# print(result[:1])


def GettingData(q):
    return{
        "place": q["properties"]["place"],
        "magnitude": q["properties"]["mag"],
        "date": str(datetime.date.fromtimestamp(q["properties"]["time"]/1000))
    }

final_result = list(map(GettingData, result))
pprint.pp(final_result)
