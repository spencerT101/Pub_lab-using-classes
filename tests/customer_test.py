import unittest
from src.customer import Customer 
from src.drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("John", 20)

    def test_customer_has_name(self):
        self.assertEqual("John", self.customer.customer_name)

    def test_customer_has_wallet(self):
        self.assertEqual(20, self.customer.customer_wallet)

    def test_remove_money_from_wallet(self):
        drink = Drink("Kronenburg", 3)
        self.assertEqual(17, self.customer.remove_money_from_wallet(drink))
    