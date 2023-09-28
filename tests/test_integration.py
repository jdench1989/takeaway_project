from lib.takeaway import *
from lib.order import *

"""
Given a customer name and order number
creates an order for that customer with a unique order number
"""
def test_create_order_with_number_and_name():
    takeaway = Takeaway()
    order_1 = takeaway.create_order(1, "Jack")
    assert order_1.order_number == 1
    assert order_1.name == "Jack"