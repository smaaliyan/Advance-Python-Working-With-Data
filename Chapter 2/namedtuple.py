import collections

# Create a point namedtuple
Point = collections.namedtuple("Point", "x y")
p1 = Point(10, 5)
p2 = Point(20, 15)
print(p1, p2)
print(p1.x, p1.y)


# Using _replace to create a new intance
p1 = p1._replace(x=15, y=10)
print(p1)