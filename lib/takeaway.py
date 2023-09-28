from lib.order import *

class Takeaway:

    def __init__(self):
        self.menu = {"Cheeseburger": 6, "Fries": 3, "Pizza": 8, "Fried chicken": 7, "Coke": 2}
        self.used_order_numbers = []

    def get_menu(self):
        return self.menu
    
    def create_order(self, order_number, name):
        return Order(order_number, name)
