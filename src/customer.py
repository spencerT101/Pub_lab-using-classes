from src.drink import Drink

class Customer:

    def __init__(self, customer_name, customer_wallet, age):

        self.customer_name = customer_name
        self.customer_wallet = customer_wallet
        self.age = age
    
    def remove_money_from_wallet(self, drink):
        self.customer_wallet -= drink.drink_price
        return self.customer_wallet
        
        

