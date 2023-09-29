from lib.order import *

"""
Given an order number and customer name
Initialises with name and number stored as attributes
and self.items as empty dict and self.total as 0
"""
def test_initialises_with_correct_values():
    order1 = Order(1, "Jack")
    assert order1.name == "Jack"
    assert order1.order_number == 1
    assert order1.items == {}
    assert order1.total == 0

"""
Given an empty order
get_menu() returns the menu as dict
"""
def test_get_menu_returns_correctly():
    order1 = Order(1, "Jack")
    assert order1.get_menu() == {"Cheeseburger": 6, "Fries": 3, "Hotdog": 5, 
                                 "Pizza": 8, "Fried chicken": 7, "Milkshake": 4, 
                                 "Coke": 2}

"""
Given multiple items
Adds items to the order and correctly calculates total
"""
def test_adds_item_and_calculates_total():
    order1 = Order(1, "Jack")
    order1.add("Hotdog")
    order1.add("Milkshake")
    assert order1.items == {"Hotdog": 5, "Milkshake": 4}
    assert order1.total == 9