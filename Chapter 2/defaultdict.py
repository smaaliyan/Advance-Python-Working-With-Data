from collections import defaultdict

fruits = ['apple', 'pear', 'banana', 'orange', 'grape', 'apple', 'banana', 'banana']


# Use a dictionary to count each elements
# FruitCounter = dict()


# Count the element in the list
# for fruit in fruits:
#     if fruit in FruitCounter.keys():
#         FruitCounter[fruit] += 1
#     else:
#         FruitCounter[fruit] = 


# Now doing the same using Default Dict

FruitCounter = defaultdict(int)
for fruit in fruits:
    FruitCounter[fruit] += 1

print(FruitCounter)