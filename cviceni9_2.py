##test_secti

import unittest

def operace(typ, a, b):
    if typ == '+':
        return a + b
    elif typ == '-':
        return a - b
    elif typ == '*':
        return a * b
    elif typ == '/':
        return a / b


class TestSecti(unittest.TestCase):
    def test_secti(self):
        self.assertEqual(operace,('+', 1, 2), 3)

    def test_odecti(self):
        self.assertEqual(operace,('-', 5, 1), 4)

    def test_vynasob(self):
        self.assertEqual(operace,('*', 2, 3), 6)

    def test_vydel(self):
        self.assertEqual(operace,('/', 2, 2), 1)