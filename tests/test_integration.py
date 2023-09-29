from lib.order_generator import *
from lib.order import *

"""
Given a customer name and order number
creates an order for that customer with assigned order number
"""
def test_create_order_with_number_and_name():
    takeaway = OrderGenerator()
    order_1 = takeaway.create_order(1, "Jack")
    assert order_1.order_number == 1
    assert order_1.name == "Jack"

# Each order created with unique order number

"""
Given a menu dict of item:cost pairs
get_menu() returns correctly
"""
def test_get_menu():
    takeaway = OrderGenerator()
    order1 = takeaway.create_order(1, "Jack")
    assert order1.get_menu() == {"Cheeseburger": 6, "Fries": 3, "Hotdog": 5, "Pizza": 8, "Fried chicken": 7, "Milkshake": 4, "Coke": 2}


"""
Given an order of multiple items
print_receipt correctly returns a formatted list of the items including the total
"""
