import unittest
from src.pub import Pub 

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00, drinks)

        def test_pub_has_name(self):
            self.assertEqual("The Prancing Pony", self.pub_name)
        
        def test_pub_has_till(self):
            self.assertEqual(100, self.pub.pub_till)
        
        def test_pub_has_drinks(self):
            self.assertEqual(drinks, self.pub.pub_drink)

        
        
