from src.drink import Drink

class Pub:

    def __init__(self, pub_name, pub_till, pub_drink):
        
        self.pub_name = pub_name
        self.pub_till = pub_till
        self.pub_drink = pub_drink

    def add_money_to_till(self, drink):
        self.pub_till += drink.drink_price
        return self.pub_till

       
# write function as defined in unit test, this time passing 2 parameters.
# call the instance pub_till and add drink price to it.
#drink class is called with (drink.) 
# add import line at top of page for drinks class.
       





