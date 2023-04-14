# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:47:21 2023

@author: Andy Turner
"""
import unittest
import calculator

class TestDocs(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(0.1, 0.1, 0.1), 0.3)

if __name__ == '__main__':
    unittest.main()