import math
import kansas  # you can import your own module
from rps7 import rock_paper_scissors

# import sys
import random as rdm  # you can rename the module and us your own name

# from enum import Enum  # only import enum from Enum module

# you can find all available modules on https://docs.python.org/3/py-modindex.html

print(math.pi)

rdm.choice("123")

for item in dir(rdm):
    print(item)

print(kansas.capital)
kansas.randomfunfact()

print(__name__)
print(kansas.__name__)

rock_paper_scissors()
