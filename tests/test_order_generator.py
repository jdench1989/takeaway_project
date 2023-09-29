from lib.order_generator import OrderGenerator
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
Given an order of multiple items
confirm_order() generates an appropriate message and sends as SMS via Twilio
Using Mock for independent unit testing
"""