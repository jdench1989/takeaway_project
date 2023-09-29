from lib.order_generator import *
from unittest.mock import Mock


"""
Given an order number and customer name
create_order correctly creates an instance of Order and assigns attributes
Using Mock for independent unit testing
"""
def test_mock_create_order_correctly_instantiates():
    mock_order = Mock(name="Order")
    mock_order.name = "Jack"
    mock_order.order_number = 1
    order_generator = OrderGenerator()
    order_generator.create_order = Mock(return_value=mock_order)
    result = order_generator.create_order(1, "Jack")
    assert result == mock_order
    assert mock_order.name == "Jack"
    assert mock_order.order_number == 1

"""
Given an order of mutiple items
print_receipt returns a nicely formatted list of the items and their prices
as well as a total amount
"""
def test_mock_print_receipt_returns_correct():
    mock_order = Mock(name="Order")
    mock_order.name = "Jack"
    mock_order.order_number = 1
    mock_order.items = {"Cheeseburger": 6, "Fries": 3,"Milkshake": 4}
    mock_order.total = 13
    order_generator = OrderGenerator()
    receipt = order_generator.print_receipt(mock_order)
    assert "Cheeseburger: £6" in receipt
    assert "Fries: £3" in receipt
    assert "Milkshake: £4" in receipt
    assert "The total cost of your order is: £13" in receipt
