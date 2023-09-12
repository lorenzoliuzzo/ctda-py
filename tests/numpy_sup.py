import numpy as np
from ctda import Quantity
from ctda import units as U

# Create a Quantity object with value=1, unit=kg.
mass = Quantity(1, U.kg)
print(mass)

# Create a Quantity object with a np.array of values, unit=m.
distance = Quantity(np.linspace(0, 10, 100), U.m)
print(distance)

x_squared = distance ** 2
print(x_squared)

# Plot the distance vs. x_squared.
import matplotlib.pyplot as plt
plt.plot(distance.value, x_squared.value)
plt.xlabel(f'x [{distance.unit}]')
plt.ylabel(f'x_squared [{x_squared.unit}]')
plt.title('Distance vs. x_squared')
plt.show()
