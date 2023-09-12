# file    scipp/physics/measurements/unit.py
# author  Lorenzo Liuzzo (lorenzoliuzzo@outlook.com)
# brief   This file contains the implementation of the Unit class.
# date    2023-07-20
# copyright Copyright (c) 2023

from .base_quantity import BaseQuantity
from .prefix import Prefix


class Unit:


    def __init__(self, base, prefix=Prefix(1), symbol=None):
        """
        Construct a Unit object with a BaseQuantity, a Prefix, and a symbol.

        :param base: The BaseQuantity associated with the Unit.
        :param prefix: The Prefix associated with the Unit. Defaults to None.
        :param symbol: The symbol associated with the Unit. Defaults to None.
        :raises TypeError: If the base parameter is not a BaseQuantity.
        """
        if isinstance(base, BaseQuantity):
            self.base = base 
        else:
            raise TypeError(f"Unsupported operand type(s) for Unit: '{type(base).__name__}' and 'BaseQuantity'")
        
        if isinstance(prefix, Prefix):
            self.prefix = prefix
        else:
            raise TypeError(f"Unsupported operand type(s) for Unit: '{type(prefix).__name__}' and 'Prefix'")
        
        self.symbol = symbol if symbol else base.__repr__()


    def __repr__(self):
        """
        Return the string representation of the Unit.

        :return: String representation of the Unit.
        """
        if self.prefix == Prefix(1):
            return f"{self.symbol}"
        else:
            return f"[{self.prefix.symbol}]{self.symbol}"


    # The following methods implement the arithmetic operations for Unit objects.

    def __mul__(self, other):
        """
        Multiply the Unit with another Unit.

        :param other: Another Unit to multiply with.
        :return: A new Unit representing the result of multiplication.
        :raises TypeError: If the operand type is not a Unit.
        """
        if isinstance(other, Unit):
            return Unit(self.base * other.base, self.prefix * other.prefix)
            
        raise TypeError(f"Unsupported operand type(s) for *: 'Unit' and '{type(other).__name__}'")

    def __truediv__(self, other):
        """
        Divide the Unit by another Unit.

        :param other: Another Unit to divide by.
        :return: A new Unit representing the result of division.
        :raises TypeError: If the operand type is not a Unit.
        """
        if isinstance(other, Unit):
            return Unit(self.base / other.base, self.prefix / other.prefix)
            
        raise TypeError(f"Unsupported operand type(s) for /: 'Unit' and '{type(other).__name__}'")

    def __pow__(self, power):
        """
        Raise the Unit to a power.

        :param power: The exponent to raise the Unit to.
        :return: A new Unit representing the result of exponentiation.
        :raises TypeError: If the operand type is not an int or a float.
        """
        if isinstance(power, (int, float)):
            return Unit(self.base ** power, self.prefix ** power)
            
        raise TypeError(f"Unsupported operand type(s) for **: 'Unit' and '{type(power).__name__}'")

    def __eq__(self, other):
        """
        Check if two Unit objects are equal.

        :param other: Another Unit object to compare with.
        :return: True if both bases and prefixes are equal, False otherwise.
        """
        return self.base == other.base and self.prefix == other.prefix

