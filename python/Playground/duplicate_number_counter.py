# create a random list of numbers from 1 to 100 and find all the duplicate numbers
# inside the list
from random import randint
from collections import Counter
l = []

for i in range(50):
    rnd = randint(0, 5)
    l.append(rnd)
x = Counter(l)
print(x)
