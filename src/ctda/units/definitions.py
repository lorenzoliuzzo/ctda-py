# file    scipp/physics/measurements/unit_definitions.py
# @author  Lorenzo Liuzzo (lorenzoliuzzo@outlook.com)
# @brief   This file contains the definitions of the most common units.
# @date    2023-07-20
# @copyright Copyright (c) 2023

from .. import Unit, Prefix, BaseQuantity
from .. import basis


# SI base quantities as units
dimensionless = Unit(basis.scalar)
m = Unit(basis.length)
s = Unit(basis.time)
kg = Unit(basis.mass)
K = Unit(basis.temperature)
A = Unit(basis.electric_current)
mol = Unit(basis.substance_amount)
cd = Unit(basis.luminous_intensity)

# SI derived units with special names and symbols
rad = Unit(basis.scalar, Prefix(1), 'rad')                          # Radian
sr = Unit(BaseQuantity(0, 0, 0, 0, 0, 0, 0), Prefix(1), 'sr')       # Steradian
Hz = Unit(basis.time ** -1, Prefix(1), 'Hz')                        # Hertz
N = Unit(BaseQuantity(1, -2, 1, 0, 0, 0, 0), Prefix(1), 'N')        # Newton
Pa = Unit(BaseQuantity(-1, -2, 1, 0, 0, 0, 0), Prefix(1), 'Pa')     # Pascal
J = Unit(BaseQuantity(2, -2, 1, 0, 0, 0, 0), Prefix(1), 'J')        # Joule
W = Unit(BaseQuantity(2, -3, 1, 0, 0, 0, 0), Prefix(1), 'W')        # Watt
C = Unit(BaseQuantity(0, 1, 0, 0, 1, 0, 0), Prefix(1), 'C')         # Coulomb
V = Unit(BaseQuantity(2, -3, 1, 0, -1, 0, 0), Prefix(1), 'V')       # Volt
F = Unit(BaseQuantity(-2, 4, -1, 0, 2, 0, 0), Prefix(1), 'F')       # Farad


km = Unit(basis.length, Prefix(1e3))    # kilometre unit
hm = Unit(basis.length, Prefix(1e2))    # hectometre unit
dam = Unit(basis.length, Prefix(1e1))   # decametre unit
dm = Unit(basis.length, Prefix(1e-1))   # decimetre unit
cm = Unit(basis.length, Prefix(1e-2))   # centimetre unit
mm = Unit(basis.length, Prefix(1e-3))   # millimetre unit
um = Unit(basis.length, Prefix(1e-6))   # micrometre unit
nm = Unit(basis.length, Prefix(1e-9))   # nanometre unit
pm = Unit(basis.length, Prefix(1e-12))  # picometre unit
# in = Unit(basis.length, Prefix(2.54e-2), 'in')    # inch unit
ft = Unit(basis.length, Prefix(30.48e-2), 'ft')   # foot unit
yd = Unit(basis.length, Prefix(91.44e-2), 'yd')   # yard unit
mi = Unit(basis.length, Prefix(1609.344e-2), 'mi')    # mile unit
nmi = Unit(basis.length, Prefix(1852e-2), 'nmi')  # nautical mile unit


m2 = Unit(basis.area)    # square metre unit

# square_kilometre = Unit(basis.area, std::kilo>; # square kilometre unit
#         inline static constexpr square_kilometre sq_km; # sq_km unit

# square_hectometre = Unit(basis.area, std::hecto>; # square hectometre unit
#         inline static constexpr square_hectometre sq_hm; # sq_hm unit

# square_centimetre = Unit(basis.area, std::centi>; # square centimetre unit
#         inline static constexpr square_centimetre sq_cm; # sq_cm unit

# square_millimetre = Unit(basis.area, std::milli>; # square millimetre unit
#         inline static constexpr square_millimetre sq_mm; # sq_mm unit

# square_micrometre = Unit(basis.area, std::micro>; # square micrometre unit
#         inline static constexpr square_micrometre sq_um; # sq_um unit

# square_nanometre = Unit(basis.area, std::nano>; # square nanometre unit
#         inline static constexpr square_nanometre sq_nm; # sq_nm unit

# hectare = Unit(basis.area, std::hecto>; # hectare unit
#         inline static constexpr hectare ha; # ha unit

# acre = Unit(basis.area, std::ratio<40468564224, 100000000>>; # acre unit
#         inline static constexpr acre ac; # ac unit

# square_mile = Unit(basis.area, std::ratio<16093440000, 1>>; # square mile unit
#         inline static constexpr square_mile sq_mi; # sq_mi unit

# square_yard = Unit(basis.area, std::ratio<83612736, 10000>>; # square yard unit
#         inline static constexpr square_yard sq_yd; # sq_yd unit

# square_foot = Unit(basis.area, std::ratio<9290304, 10000>>; # square foot unit
#         inline static constexpr square_foot sq_ft; # sq_ft unit

# square_inch = Unit(basis.area, std::ratio<64516, 10000>>; # square inch unit
#         inline static constexpr square_inch sq_in; # sq_in unit


# cubic_metre = Unit(basis.volume>; # cubic metre unit
#         inline static constexpr cubic_metre cu_m; # cu_m unit

# cubic_millimetre = Unit(basis.volume, std::milli>; # cubic millimetre unit
#         inline static constexpr cubic_millimetre cu_mm; # cu_mm unit

# cubic_centimetre = Unit(basis.volume, std::centi>; # cubic centimetre unit
#         inline static constexpr cubic_centimetre cu_cm; # cu_cm unit

# cubic_decimetre = Unit(basis.volume, std::deci>; # cubic decimetre unit
#         inline static constexpr cubic_decimetre cu_dm; # cu_dm unit

# cubic_kilometre = Unit(basis.volume, std::kilo>; # cubic kilometre unit
#         inline static constexpr cubic_kilometre cu_km; # cu_km unit

# litre = cubic_decimUtre( 
#         inli. static constexpr litre L; # L unit

# decilitre = Uath(:.::multiply_t<std::deci, litre>; 
#         inline static constexpr decilitre dL; 

# centilitre = Uath(:.::multiply_t<std::centi, litre>; 
#         inline static constexpr centilitre cL; 

# millilitre = Uath(:.::multiply_t<std::milli, litre>; 
#         inline static constexpr millilitre mL; 

# decalitre = Uath(:.::multiply_t<std::deca, litre>; 
#         inline static constexpr decalitre daL; # daL unit

# hectolitre = Uath(:.::multiply_t<std::hecto, litre>; # hectolitre unit
#         inline static constexpr hectolitre hL; # hL unit

# kilolitre = Uath(:.::multiply_t<std::kilo, litre>; # kilolitre unit
#         inline static constexpr kilolitre kL; # kL unit


# decisecond = Unit(basis.time, std::deci>; # decisecond unit
#         inline static constexpr decisecond ds; # ds unit

# centisecond = Unit(basis.time, std::centi>; # centisecond unit
#         inline static constexpr centisecond cs; # cs unit
        
# millisecond = Unit(basis.time, std::milli>; # millisecond unit
#         inline static constexpr millisecond ms; # ms unit

# microsecond = Unit(basis.time, std::micro>; # microsecond unit
#         inline static constexpr microsecond us; # us unit

# nanosecond = Unit(basis.time, std::nano>; # nanosecond unit
#         inline static constexpr nanosecond ns; # ns unit

# picosecond = Unit(basis.time, std::pico>; # picosecond unit
#         inline static constexpr picosecond ps; # ps unit

# minute = Unit(basis.time, std::ratio<60>>; # minute unit
#         inline static constexpr minute min; # min unit

# hour = Unit(basis.time, std::ratio<3600>>; # hour unit
#         inline static constexpr hour h; # h unit

# day = Unit(basis.time, std::ratio<86400>>; # day unit
#         inline static constexpr day d; # d unit

# week = Unit(basis.time, std::ratio<604800>>; # week unit
#         inline static constexpr week wk; # wk unit

# year = Unit(basis.time, std::ratio<31557600>>; # year unit
#         inline static constexpr year yr; # yr unit


# kilogram = Unit(basis.mass>; # kilogram unit
#         inline static constexpr kilogram kg; # kg unit

# gram = Unit(basis.mass, std::milli>; # gram unit
#         inline static constexpr gram g; # g unit

# milligram = Unit(basis.mass, std::micro>; # milligram unit
#         inline static constexpr milligram mg; # mg unit

# microgram = Unit(basis.mass, std::nano>; # microgram unit
#         inline static constexpr microgram ug; # ug unit

# tonne = Unit(basis.mass, std::kilo>; # tonne unit
#         inline static constexpr tonne t; # t unit

# pound = Unit(basis.mass, std::ratio<45359237, 100000000>>; # pound unit
#         inline static constexpr pound lb; # lb unit

# ounce = Unit(basis.mass, std::ratio<28349523, 1000000000>>; # ounce unit
#         inline static constexpr ounce oz; # oz unit


# joule = Unit(basis.energy>; # joule unit
#         inline static constexpr joule J; # J unit

# millijoule = Unit(basis.energy, std::milli>; # millijoule unit
#         inline static constexpr millijoule mJ; # mJ unit

# microjoule = Unit(basis.energy, std::micro>; # microjoule unit
#         inline static constexpr microjoule uJ; # uJ unit

# nanojoule = Unit(basis.energy, std::nano>; # nanojoule unit
#         inline static constexpr nanojoule nJ; # nJ unit

# kilojoule = Unit(basis.energy, std::kilo>; # kilojoule unit
#         inline static constexpr kilojoule kJ; # kJ unit

# megajoule = Unit(basis.energy, std::mega>; # megajoule unit
#         inline static constexpr megajoule MJ; # MJ unit

# gigajoule = Unit(basis.energy, std::giga>; # gigajoule unit
#         inline static constexpr gigajoule GJ; # GJ unit

# electronvolt = Unit(basis.energy, std::pico>; # electronvolt unit
#         inline static constexpr electronvolt eV; # eV unit

# kiloelectronvolt = Unit(basis.energy, std::femto>; # kiloelectronvolt unit
#         inline static constexpr kiloelectronvolt keV; # keV unit

# megaelectronvolt = Unit(basis.energy, std::atto>; # megaelectronvolt unit
#         inline static constexpr megaelectronvolt MeV; # MeV unit

# calorie = Unit(basis.energy, std::ratio<4184, 1000>>; # calorie unit
#         inline static constexpr calorie cal; # cal unit

# kilocalorie = Unit(basis.energy, std::ratio<4184, 1>>; # kilocalorie unit
#         inline static constexpr kilocalorie kcal; # kcal unit
        

# newton = Unit(basis.force>; # newton unit
#         inline static constexpr newton N; # N unit

# kilonewton = Unit(basis.force, std::kilo>; # kilonewton unit
#         inline static constexpr kilonewton kN; # kN unit

#         pound_force = Unit(basis.force, std::ratio<4448222, 10000>>; # pound-force unit
#         // inline static constexpr pound_force lbf; # lbf unit

# pascal = Unit(basis.pressure>; # pascal unit
#         inline static constexpr pascal Pa; # m2 unit

# kilopascal = Unit(basis.pressure, std::kilo>; # kilopascal unit
#         inline static constexpr kilopascal kPa; # kPa unit

# megapascal = Unit(basis.pressure, std::mega>; # megapascal unit
#         inline static constexpr megapascal MPa; # MPa unit

# gigapascal = Unit(basis.pressure, std::giga>; # gigapascal unit
#         inline static constexpr gigapascal GPa; # GPa unit

# barometre = Unit(basis.pressure, std::ratio<100000, 1>>; # bar unit
#         inline static constexpr barometre bar; # bar unit

# millibar = Unit(basis.pressure, std::ratio<100, 1>>; # millibar unit
#         inline static constexpr millibar mbar; # mbar unit

# atmosphere = Unit(basis.pressure, std::ratio<101325, 1>>; # atmosphere unit
#         inline static constexpr atmosphere atm; # atm unit

# torricelli = Unit(basis.pressure, std::ratio<101325, 760>>; # torr unit
#         inline static constexpr torricelli torr; # torr unit


# kelvin = Unit(basis.temperature>;
#         inline static constexpr kelvin K;


# mole = Unit(basis.substance_amount>;
#         inline static constexpr mole mol;
