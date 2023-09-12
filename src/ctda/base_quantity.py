
class BaseQuantity:


    def __init__(self, length, time, mass, temperature, electric_current, substance_amount, luminous_intensity):
        """
        Construct a BaseQuantity object with dimensional information for a physical quantity.
        It uses the SI base units as a reference for each dimension.

        :param length: Power of length.
        :param time: Power of time.
        :param mass: Power of mass.
        :param temperature: Power of temperature.
        :param electric_current: Power of electric current.
        :param substance_amount: Power of substance amount.
        :param luminous_intensity: Power of luminous intensity.
        """
        self.quantity_info = {
            'm': length,
            's': time,
            'kg': mass,
            'K': temperature,
            'A': electric_current,
            'mol': substance_amount,
            'cd': luminous_intensity
        }


    def __repr__(self):
        # Return the string representation of the BaseQuantity.
        return "".join(
            [f"{unit}" if power == 1 else f"{unit}^{power}" 
            for unit, power in self.quantity_info.items() if power != 0]
        )
    

    # The following methods implement the arithmetic operations for BaseQuantity objects.
    
    def __mul__(self, other):
        """
        Multiply the BaseQuantity with another BaseQuantity.

        :param other: Another BaseQuantity to multiply with.
        :return: A new BaseQuantity representing the result of multiplication.
        :raises TypeError: If the operand type is not a BaseQuantity.
        """
        if isinstance(other, BaseQuantity):
            return BaseQuantity(
                self.quantity_info['m'] + other.quantity_info['m'],
                self.quantity_info['s'] + other.quantity_info['s'],
                self.quantity_info['kg'] + other.quantity_info['kg'],
                self.quantity_info['K'] + other.quantity_info['K'],
                self.quantity_info['A'] + other.quantity_info['A'],
                self.quantity_info['mol'] + other.quantity_info['mol'],
                self.quantity_info['cd'] + other.quantity_info['cd']
            )
 
        raise TypeError("Unsupported operand type(s) for *: 'BaseQuantity' and '{}'".format(type(other).__name__))

    def __truediv__(self, other):
        """
        Divide the BaseQuantity by another BaseQuantity.

        :param other: Another BaseQuantity to divide by.
        :return: A new BaseQuantity representing the result of division.
        :raises TypeError: If the operand type is not a BaseQuantity.
        """
        if isinstance(other, BaseQuantity):
            return BaseQuantity(
                self.quantity_info['m'] - other.quantity_info['m'],
                self.quantity_info['s'] - other.quantity_info['s'],
                self.quantity_info['kg'] - other.quantity_info['kg'],
                self.quantity_info['K'] - other.quantity_info['K'],
                self.quantity_info['A'] - other.quantity_info['A'],
                self.quantity_info['mol'] - other.quantity_info['mol'],
                self.quantity_info['cd'] - other.quantity_info['cd']
            )
 
        raise TypeError("Unsupported operand type(s) for /: 'BaseQuantity' and '{}'".format(type(other).__name__))

    def __pow__(self, power):
        """
        Raise the BaseQuantity to a power.

        :param power: The exponent to raise the BaseQuantity to.
        :return: A new BaseQuantity representing the result of exponentiation.
        :raises TypeError: If the operand type is not an int or a float.
        """
        if isinstance(power, (int, float)):
                
            return BaseQuantity(
                self.quantity_info['m'] * power,
                self.quantity_info['s'] * power,
                self.quantity_info['kg'] * power,
                self.quantity_info['K'] * power,
                self.quantity_info['A'] * power,
                self.quantity_info['mol'] * power,
                self.quantity_info['cd'] * power
            )

        raise TypeError("Unsupported operand type(s) for **: 'BaseQuantity' and '{}'".format(type(power).__name__))

    def __eq__(self, other):
        # Check if two BaseQuantity objects are equal.
        return self.quantity_info == other.quantity_info
