# 45 Packages
from ecommerce.shipping import calc_shipping
# from ecommeerce import shipping
# shipping.calc_shipping()
calc_shipping()

# 46 Generating Random Values
import random

# for i in range(3):
#     print(random.randint(1, 30000))

people = ["J", "B", "T", "G"]
leader = random.choice(people)
print(leader)


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return (first, second) # You can remove the braces of the tuple
                               # because Python will automatically
                               # recognize this as a tuple (not list)


dice = Dice()
print(dice.roll())

# 47 Directories
from pathlib import Path

path = Path()
print(path.exists()) # checks if directory exists
# print(path.mkdir()) # make directory
# print(path.rmdir()) # remove directory
for file in path.glob('*'):
    print(file)

# 48 Pypi and Pip
# https://pypi.org/
# Search and import libraries
