from lib.takeaway import *

"""
Given a menu of item:cost pairs
get_menu() returns correctly
"""
def test_get_menu():
    takeaway = Takeaway()
    assert takeaway.menu == {"Cheeseburger": 6, "Fries": 3, "Pizza": 8, "Fried chicken": 7, "Coke": 2}

"""
"""