#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc1 (unittest.TestCase):

        def test1 (self):
                self.assertEqual (100, calc(10,10))

	def test2 (self):
                self.assertEqual (-1, calc(500,200.2))

	def test3 (self):
                self.assertEqual (-1, calc(200.2,500))

        def test4 (self):
                self.assertEqual (-1, calc(0.9,34))

        def test5 (self):
                self.assertEqual (-1, calc(29,0.9))

	def test6 (self):
                self.assertEqual (555, calc(1,555))

        def test7 (self):
                self.assertEqual (880, calc(880,1))

        def test8 (self):
                self.assertEqual (-1, calc(999.1,42))

	def test9 (self):
                self.assertEqual (-1, calc(68,999.1))

	def test10 (self):
                self.assertEqual (49950, calc(999,50))

        def test11 (self):
                self.assertEqual (49950, calc(50,999))

        def test12 (self):
                self.assertEqual (-1, calc('a','b'))

        def test13 (self):
                self.assertEqual (-1, calc('a',532))

        def test14 (self):
                self.assertEqual (-1, calc(33,'b'))
