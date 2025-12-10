from cviceni6 import fibonacci
import unittest

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        vysledek = fibonacci(2)
        self.assertEqual(vysledek, [1, 1, 2])

        self.assertEqual(fibonacci(10), [1, 1, 2, 3, 5, 8])


    #NEFUNGUJE FIBONACCI, TO JE BLBY CO.... SPATNE VE CVICENI6.PY
    ... # dalsi testy muze byt pridany zde