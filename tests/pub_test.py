import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
#from src.food import Food

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00, "Kronenburg")

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.pub_name)
        
    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.pub_till)
        
    def test_pub_has_drinks(self):
        self.assertEqual("Kronenburg", self.pub.pub_drink)

    def test_money_added_to_till(self):
        drink = Drink("Kronenburg", 3)
        self.assertEqual(103, self.pub.add_money_to_till(drink))
        # define function test.
        # define what result we want to see pub till = 103.
        # inside assertEqual () add integer, and function to call from pub class
        # self.pub tells the unit test to access the till in the Pub class and call the till with the value stored in Drink.
    
    def test_age_verification(self):
        customer = Customer("John", 20, 18)
        self.assertEqual(True, self.pub.check_age(customer))
    

