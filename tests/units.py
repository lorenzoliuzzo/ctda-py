# @file: tests/units.py 
# @auth: Lorenzo Liuzzo
# @date: 2021-07-21
# @desc: Test the units module of the physics package

from ctda import Prefix, Unit
from ctda import basis as basis
from ctda import units as units


# Creating a unit
metre = Unit(basis.length); 
print(metre)

# Creating a unit with a prefix
millimetre = Unit(basis.length, Prefix(1e-3))
print(millimetre)

# Creating a composed unit with a special symbol
metre_second = Unit(basis.length / basis.time, symbol="m/s")
print(metre_second)

print(millimetre * metre_second)
print(metre ** 2)
print(metre_second ** 2)    
print(millimetre ** 2)  
print(millimetre ** 3)  

# Using the predefined units
print(units.m)
print(units.s)