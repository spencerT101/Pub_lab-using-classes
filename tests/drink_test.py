import unittest
from src.drink import Drink 

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Kronenburg", 3)

    def test_drink_has_name(self):

        self.assertEqual("Kronenburg", self.drink_name)
    
    def drink_has_price(self):

        self.assertEqual(3, self.drink_price)

        



        