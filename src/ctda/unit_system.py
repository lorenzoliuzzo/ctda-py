
class BaseQuantity: 

    def __init__(self, name: str, powers: list[int], unit_symbol: str = None) -> None:
        self.name = name
        self.powers = powers
        self.unit_symbol = unit_symbol

    def __repr__(self) -> str:
        if self.unit_symbol is not None:
            return self.name + " [" + self.unit_symbol + "]"
        else: 
            return self.name
        
    def __mul__(self, other): 
        if isinstance(other, BaseQuantity) and len(other.powers) == len(self.powers):
            result = BaseQuantity(
                name=(self.name + '^2' if other.name == self.name 
                        else self.name if other.name == "scalar" 
                            else other.name if self.name == "scalar" 
                                else self.name + ' * ' + other.name), 
                powers=list(self.powers[i] + other.powers[i] for i in range(0, len(self.powers)))
            )

            if (self.unit_symbol != None and other.unit_symbol != None):
                if self.unit_symbol == other.unit_symbol:
                    result.unit_symbol = self.unit_symbol + '^2'
                else:
                    result.unit_symbol = self.unit_symbol + '*' + other.unit_symbol    
            elif self.unit_symbol != None:
                result.unit_symbol = self.unit_symbol
            else:
                result.unit_symbol = other.unit_symbol

            return result
        
        else: 
            raise TypeError("Unsupported operand type(s) for *: 'BaseQuantity' and '{}'".format(type(other).__name__))
        

    def __truediv__(self, other): 
        if isinstance(other, BaseQuantity) and len(other.powers) == len(self.powers):
            result = BaseQuantity(
                name=("scalar" if self.name == other.name
                        else self.name if other.name == "scalar"
                            else self.name + ' / ' + other.name), 
                powers=list(self.powers[i] - other.powers[i] for i in range(0, len(self.powers))),
            )

            if (self.unit_symbol != None and other.unit_symbol != None):
                if self.unit_symbol != other.unit_symbol:
                    result.unit_symbol = self.unit_symbol + '/' + other.unit_symbol
            elif self.unit_symbol != None:
                result.unit_symbol = self.unit_symbol   
            else:
                result.unit_symbol = other.unit_symbol + '^-1'

            return result

        else: 
            raise TypeError("Unsupported operand type(s) for *: 'BaseQuantity' and '{}'".format(type(other).__name__))
        
    
    def __pow__(self, power): 
        return BaseQuantity(
            name=(self.name if power == 1 else self.name + '^' + str(power)), 
            powers=list(self.powers[i] * power for i in range(0, len(self.powers))),
            unit_symbol=(self.unit_symbol + '^' + str(power) if self.unit_symbol != None else None)
        )
    

class UnitSystem:

    def __init__(self, name, basis) -> None:
        self.name = name
        self.ndim = len(basis)
        if all(len(base.powers) == self.ndim for base in basis):
            self.dimensions = basis 
        else: 
            raise ValueError("Cannot create an UnitSystem with vectors of different size as basis.")


prefix_literals = {
    1e24:  'Y',  # Yotta
    1e21:  'Z',  # Zetta
    1e18:  'E',  # Exa
    1e15:  'P',  # Peta
    1e12:  'T',  # Tera
    1e9:   'G',  # Giga
    1e6:   'M',  # Mega
    1e3:   'k',  # Kilo
    1e2:   'h',  # Hecto
    1e1:   'D',  # Deca
    1e-1:  'd',  # Deci
    1e-2:  'c',  # Centi
    1e-3:  'm',  # Milli
    1e-6:  'u',  # Micro
    1e-9:  'n',  # Nano
    1e-12: 'p',  # Pico
    1e-15: 'f',  # Femto
    1e-18: 'a',  # Atto
    1e-21: 'z',  # Zepto
    1e-24: 'y'   # Yocto
}


class Unit:
    
    def __init__(self, unit_system: UnitSystem, name: str, base: BaseQuantity, factor = 1) -> None:
        self.system = unit_system
        self.name = name

        if self.system.ndim == len(base.powers): 
            self.base = base
        else:
            raise TypeError(f"Cannot construct an unit of the '{self.system.name}' system with a BaseQuantity of different dimension: {len(base.powers)} instead of {self.system.ndim} dimensions.")
        
        self.factor = factor
        
    def __repr__(self) -> str:
        base_symbol = prefix_symbol = ""

        if self.factor != 1:
            if self.factor in prefix_literals:
                prefix_symbol = prefix_literals[self.factor]
            else: 
                raise ValueError("Cannot find a suitable prefix representation for a factor of ", self.factor)
        
        if self.base.unit_symbol is not None:
            base_symbol = self.base.unit_symbol
        else: 
            for i in range(0, self.system.ndim):
                if self.base.powers[i] != 0:
                    base_symbol += self.system.dimensions[i].name
                    if self.base.powers[i] != 1: 
                        base_symbol += '^' + str(self.base.powers[i])
                        
        return prefix_symbol + base_symbol
    

    def __mul__(self, other): 
        if isinstance(other, Unit) and self.system == other.system:
            return Unit(
                name=(self.name + ' * ' + other.name),
                unit_system=self.system,
                base=self.base * other.base,
                factor=self.factor * other.factor
            )
        else: 
            raise TypeError("Unsupported operand type(s) for *: 'Unit' and '{}'".format(type(other).__name__))
        
    def __truediv__(self, other): 
        if isinstance(other, Unit) and self.system == other.system:
            return Unit(
                name=(self.name + ' / ' + other.name),
                unit_system=self.system,
                base=self.base / other.base,
                factor=self.factor / other.factor
            )
        else:
            raise TypeError("Unsupported operand type(s) for /: 'Unit' and '{}'".format(type(other).__name__))
        
    def __pow__(self, power):
        return Unit(
            name=(self.name if power == 1 else self.name + '^' + str(power)), 
            unit_system=self.system,
            base=self.base ** power,
            factor=self.factor ** power
        )
        

length =                BaseQuantity(name="length",               powers=[1, 0, 0, 0, 0, 0, 0], unit_symbol="m")
mass =                  BaseQuantity(name="mass",                 powers=[0, 1, 0, 0, 0, 0, 0], unit_symbol="kg")
time =                  BaseQuantity(name="time",                 powers=[0, 0, 1, 0, 0, 0, 0], unit_symbol="s")
temperature =           BaseQuantity(name="temperature",          powers=[0, 0, 0, 1, 0, 0, 0], unit_symbol="K")
electric_current =      BaseQuantity(name="electric current",     powers=[0, 0, 0, 0, 1, 0, 0], unit_symbol="A")
substance_amount =      BaseQuantity(name="substance amount",     powers=[0, 0, 0, 0, 0, 1, 0], unit_symbol="mol")
luminous_intensity =    BaseQuantity(name="luminous intensity",   powers=[0, 0, 0, 0, 0, 0, 1], unit_symbol="cd")

angle =                 BaseQuantity(name="angle",                powers=[0, 0, 0, 0, 0, 0, 0],  unit_symbol="rad")
velocity =              BaseQuantity(name="velocity",             powers=[1, 0, -1, 0, 0, 0, 0], unit_symbol="m/s")
acceleration =          BaseQuantity(name="acceleration",         powers=[1, 0, -2, 0, 0, 0, 0], unit_symbol="m/s^2")
angular_velocity =      BaseQuantity(name="angular velocity",     powers=[0, 0, -1, 0, 0, 0, 0], unit_symbol="rad/s")
angular_acceleration =  BaseQuantity(name="angular acceleration", powers=[0, 0, -1, 0, 0, 0, 0], unit_symbol="rad/s^2")
momentum =              BaseQuantity(name="momentum",             powers=[1, 1, -1, 0, 0, 0, 0], unit_symbol="kg*m/s")
angular_momentum =      BaseQuantity(name="angular momentum",     powers=[0, 1, -1, 0, 0, 0, 0], unit_symbol="kg*rad/s")


SI = UnitSystem(name="SI", basis=[length, mass, time, temperature, electric_current, substance_amount, luminous_intensity])

dimensionless = Unit(unit_system=SI, name="scalar", base=BaseQuantity(name="scalar", powers=[0, 0, 0, 0, 0, 0, 0]))

metre = Unit(unit_system=SI, name="metre", base=length)
kilogram = Unit(unit_system=SI, name="kilogram", base=mass)
second = Unit(unit_system=SI, name="second", base=time)
kelvin = Unit(unit_system=SI, name="kelvin", base=temperature)
ampere = Unit(unit_system=SI, name="ampere", base=electric_current)
mole = Unit(unit_system=SI, name="mole", base=substance_amount)
candela = Unit(unit_system=SI, name="candela", base=luminous_intensity)

newton = Unit(SI, "Newton", BaseQuantity(name="force", powers=[1, 1, -2, 0, 0, 0, 0], unit_symbol="N"))
millinewton = Unit(SI, "Newton", BaseQuantity(name="force", powers=[1, 1, -2, 0, 0, 0, 0], unit_symbol="N"), factor=1e-3)


print(length)                       # output: length [m]
print(length * mass)                # output: length * mass [m*kg]
print(length * length * mass)       # output: length^2 * mass [m^2*kg]
print(length / length)              # output: scalar
print(length / length / length)     # output: scalar / length [m^-1]
print(length / length * time)       # output: time [s]
print(length * time / length)       # desired output: time [s] # output is: length * time / length [m*s/m]

# print((length * time) / length) # output: time [s]
# print(length / time) # output: length / time [m/s]
# print(length ** 2)

print(metre)
print(metre * second)
print(metre / second)
print(metre ** 2)

xunit = metre * metre * kelvin / metre

print(xunit)
print(xunit.base.powers)


import numpy as np


# Class representing a physical quantity with a numerical value and a specific unit.
class Quantity:

    def __init__(self, value, unit: Unit = dimensionless):
        """
        Construct a Quantity object with a given numerical value and an associated Unit.

        :param value: The numerical value of the quantity.
        :param unit: The Unit object representing the unit of the quantity.
        """
        if isinstance(value, np.ndarray):
            if np.all(isinstance(item, Quantity) for item in value):
                    # print(value)
                # If value is an ndarray of Quantity objects
                # if np.all(item.unit == value[0].unit for item in value):
                    self.value = np.array([item for item in value])
                    self.unit = unit
                # else:
                #     raise ValueError("Incompatible units")
            
            else:
                # If value is a generic ndarray
                self.value = value
                self.unit = unit

        else:
            self.value = np.array([value])
            self.unit = unit


    def __repr__(self):
        # Return the string representation of the Quantity.
        return f"{self.value} {self.unit}"
    

position3 = Quantity(np.array([1, 2, 3]), metre)
print(position3)