# "DEQUE" short for "double ended queue" pronounce ad "DECK"

from collections import deque
import string

# Initialize a deque with lowercase letters
d = deque(string.ascii_lowercase)
# print(d)


# Deque also supports the len() functions
print(f"Item Count: {len(d)}")

# Deque can be iterated over
for elemnet in d:
    print(elemnet.upper())

# Manipulate items from either end
d.pop()
d.popleft()
d.append(1)
d.appendleft(26)
print(d)

# Use an index to get a perticular item
print(d)
d.rotate(-2)
print(d)

