# @file: tests/quantity.py 
# @auth: Lorenzo Liuzzo
# @date: 2021-07-22
# @desc: Test the Quantity class of the physics package

import unittest
from physics import Quantity
from physics import units as U
import numpy as np


class TestQuantityOperations(unittest.TestCase):

    def test_addition(self):
        a = Quantity(2, U.m)
        b = Quantity(1, U.m)
        c = a + b
        self.assertEqual(c.value, 3)  
        self.assertEqual(c.unit, U.m)  

        c = Quantity(np.array([1, 2, 3]), U.m)
        d = Quantity(np.array([4, 5, 6]), U.m)
        e = c + d
        self.assertTrue(np.array_equal(e.value, np.array([5, 7, 9])))  
        self.assertEqual(e.unit, U.m)

        f = a + c
        self.assertTrue(np.array_equal(f.value, np.array([3, 4, 5])))  
        self.assertEqual(f.unit, U.m)


    def test_subtraction(self):
        a = Quantity(2, U.m)
        b = Quantity(1, U.m)
        c = a - b
        self.assertEqual(c.value, 1)  
        self.assertEqual(c.unit, U.m)  

        c = Quantity(np.array([1, 2, 3]), U.m)
        d = Quantity(np.array([4, 5, 6]), U.m)
        e = c - d
        self.assertTrue(np.array_equal(e.value, np.array([-3, -3, -3])))  
        self.assertEqual(e.unit, U.m)

        f = a - c
        self.assertTrue(np.array_equal(f.value, np.array([1, 0, -1])))  
        self.assertEqual(f.unit, U.m)

    def test_multiplication(self):
        a = Quantity(2, U.m)
        b = Quantity(3, U.s)
        c = a * b
        self.assertEqual(c.value, 6)  
        self.assertEqual(c.unit, U.m * U.s)  

        d = Quantity(np.array([1, 2, 3]), U.m)
        e = Quantity(np.array([4, 5, 6]), U.m)
        f = d * e
        self.assertTrue(np.array_equal(f.value, np.array([4, 10, 18])))
        self.assertEqual(f.unit, U.m ** 2)

        g = a * d
        self.assertTrue(np.array_equal(g.value, np.array([2, 4, 6])))
        self.assertEqual(g.unit, U.m ** 2)


    def test_division(self):
        a = Quantity(10, U.m)
        b = Quantity(2, U.s)
        c = a / b
        self.assertEqual(c.value, 5)  
        self.assertEqual(c.unit, U.m / U.s)  

        d = Quantity(np.array([1, 2, 3]), U.m)
        e = Quantity(np.array([4, 5, 6]), U.m)
        f = d / e
        self.assertTrue(np.array_equal(f.value, np.array([0.25, 0.4, 0.5])))
        self.assertEqual(f.unit, U.dimensionless)

        g = a / d
        self.assertTrue(np.array_equal(g.value, np.array([10, 5, 10/3])))
        self.assertEqual(g.unit, U.dimensionless)


    def test_power(self):
        a = Quantity(3, U.m)
        b = a ** 2
        self.assertEqual(b.value, 9)  
        self.assertEqual(b.unit, U.m ** 2)  

        c = b ** 0.5
        self.assertEqual(c.value, 3)  
        self.assertEqual(c.unit, U.m)  

        d = Quantity(np.array([1, 2, 3]), U.m)
        e = d ** 2
        self.assertTrue(np.array_equal(e.value, np.array([1, 4, 9])))
        self.assertEqual(e.unit, U.m ** 2)

        f = e ** 0.5
        self.assertTrue(np.array_equal(f.value, np.array([1, 2, 3])))
        self.assertEqual(f.unit, U.m)


    def test_sin(self):
        a = Quantity(0, U.rad)
        b = np.sin(a)
        self.assertEqual(b.value, 0)
        self.assertEqual(b.unit, U.dimensionless)

        c = Quantity(np.array([0, np.pi/2, 0]), U.rad)
        d = np.sin(c)
        self.assertTrue(np.array_equal(d.value, np.array([0, 1, 0])))
        self.assertEqual(d.unit, U.dimensionless)

    def test_arcsin(self):
        a = Quantity(0)
        b = np.arcsin(a)
        self.assertEqual(b.value, 0)
        self.assertEqual(b.unit, U.rad)

        c = Quantity(np.array([0, 1/2, 1]), U.rad)
        d = np.arcsin(c)
        self.assertTrue(np.isclose(d.value, np.array([0, np.pi/6, np.pi/2])).all())
        self.assertEqual(d.unit, U.rad)



    def test_cos(self):
        a = Quantity(0, U.rad)
        b = np.cos(a)
        self.assertEqual(b.value, 1)
        self.assertEqual(b.unit, U.dimensionless)

        c = Quantity(np.array([0, -np.pi, np.pi]), U.rad)
        d = np.cos(c)
        self.assertTrue(np.array_equal(d.value, np.array([1, -1, -1])))
        self.assertEqual(d.unit, U.dimensionless)

    def test_arccos(self):
        a = Quantity(0)
        b = np.arccos(a)
        self.assertEqual(b.value, np.pi/2)
        self.assertEqual(b.unit, U.rad)

        c = Quantity(np.array([0, -1, 1]), U.rad)
        d = np.arccos(c)
        self.assertTrue(np.isclose(d.value, np.array([np.pi/2, np.pi, 0])).all())
        self.assertEqual(d.unit, U.rad)


    def test_tan(self):
        a = Quantity(0, U.rad)
        b = np.tan(a)
        self.assertEqual(b.value, 0)
        self.assertEqual(b.unit, U.dimensionless)

        c = Quantity(np.array([0, np.pi/4, -np.pi/4]), U.rad)
        d = np.tan(c)
        self.assertTrue(np.isclose(d.value, np.array([0, 1, -1])).all())
        self.assertEqual(d.unit, U.dimensionless)

    def test_arctan(self):
        a = Quantity(0)
        b = np.arctan(a)
        self.assertEqual(b.value, 0)
        self.assertEqual(b.unit, U.rad)

        c = Quantity(np.array([0, 1, -1]), U.rad)
        d = np.arctan(c)
        self.assertTrue(np.isclose(d.value, np.array([0, np.pi/4., -np.pi/4.])).all())
        self.assertEqual(d.unit, U.rad)


if __name__ == "__main__":
    unittest.main()
