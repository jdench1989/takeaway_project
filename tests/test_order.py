from lib.order import *

"""
Given a order number and customer name
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
Given multiple items
Adds items to the order and correctly calculates total
"""
def test_adds_item_and_calculates_total():
    order1 = Order(1, "Jack")
    order1.add({"Hotdog": 3})
    order1.add({"Milkshake": 2})
    assert order1.items == {"Hotdog": 3, "Milkshake": 2}
    assert order1.total == 5