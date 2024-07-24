from collections import Counter

class1 = ["Aaliyan", "Owais", "Rayyan", "Hammad", "Shafiq", "Shabir", "Anus", 'Aaliyan']
class2 = ["Shumaim", "Osama", "Arham", "Aaliyan", "Waqar", "Hamza", "Owais", "Shayan"]

# Creating a counter for both the classes
c1 = Counter(class1)
c2 = Counter(class2)

# How many students in class 1 and class 2 named 'Aaliyan'
print(c1["Aaliyan"])
print(c2["Aaliyan"])

# How many students are in class 1 and class 2
print(sum(c1.values()), "students in class 1")
print(sum(c2.values()), "students in class 2")

# Combining both the classes
c1.update(c2)
print(sum(c1.values()), "students are total in both classes")

# What is the most common name in both classes
print(c1.most_common(3))

# Seperating the classes again
c1.subtract(c2)
print(sum(c1.values()))

# What is the common between both the classes
print(c1 & c2)