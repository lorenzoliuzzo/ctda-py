# @file: tests/basis.py 
# @auth: Lorenzo Liuzzo
# @date: 2021-07-21
# @desc: Test the basis module of the physics package

from ctda import BaseQuantity
from ctda import basis as basis

# Creating a base quantity
length = BaseQuantity(1, 0, 0, 0, 0, 0, 0)
print(length)

time = BaseQuantity(0, 1, 0, 0, 0, 0, 0)
print(time)

# Creating a composed base quantity
velocity = length / time
print(velocity)

# Using the predefined base quantities from basis
print(basis.length)
print(basis.time)
print(basis.velocity)
print(basis.force)