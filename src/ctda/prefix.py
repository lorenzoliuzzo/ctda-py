# file    scipp/physics/measurements/prefix.py
# author  Lorenzo Liuzzo (lorenzoliuzzo@outlook.com)
# brief   This file contains the implementation of the BaseQuantity class.
# date    2023-07-20
# copyright Copyright (c) 2023


prefix_table = {
    'Y': 1e24,  # Yotta
    'Z': 1e21,  # Zetta
    'E': 1e18,  # Exa
    'P': 1e15,  # Peta
    'T': 1e12,  # Tera
    'G': 1e9,   # Giga
    'M': 1e6,   # Mega
    'k': 1e3,   # Kilo
    'h': 1e2,   # Hecto
    'da': 1e1,  # Deca
    'd': 1e-1,  # Deci
    'c': 1e-2,  # Centi
    'm': 1e-3,  # Milli
    'u': 1e-6,  # Micro
    'n': 1e-9,  # Nano
    'p': 1e-12, # Pico
    'f': 1e-15, # Femto
    'a': 1e-18, # Atto
    'z': 1e-21, # Zepto
    'y': 1e-24  # Yocto
}


class Prefix:


    def __init__(self, factor):
        """
        Construct a Prefix object with a given factor.

        :param factor: The factor of the prefix.
        """
        self.factor = factor
        for symbol, multiplier in prefix_table.items():
            if factor == multiplier: 
                self.symbol = symbol 
                break
        else:
            self.symbol = None
                

    def __repr__(self):
        # Return the string representation of the Prefix.
        if self.symbol != None:
            return f"[{self.symbol}]"
    

    # The following methods implement the arithmetic operations for Prefix objects.
    def __mul__(self, other):
        """
        Multiply the Prefix with another Prefix.

        :param other: Another Prefix to multiply with.
        :return: A new Prefix representing the result of multiplication.
        """
        return Prefix(self.factor * other.factor)
    
    def __truediv__(self, other):
        """
        Divide the Prefix with another Prefix.

        :param other: Another Prefix to divide with.
        :return: A new Prefix representing the result of division.
        """
        return Prefix(self.factor / other.factor)
    
    def __pow__(self, power):
        """
        Raise the Prefix to a power.

        :param power: The exponent to raise the Prefix to.
        :return: A new Prefix representing the result of exponentiation.
        """
        return Prefix(self.factor ** power)
    
    def __eq__(self, other):
        # Check if two Prefix objects are equal.
        return self.factor == other.factor
        