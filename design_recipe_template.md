Takeaway Service Multi-Class Planned Design Recipe
1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

    As a customer
    So that I can check if I want to order something
    I would like to see a list of dishes with prices.

    As a customer
    So that I can order the meal I want
    I would like to be able to select some number of several available dishes.

    As a customer
    So that I can verify that my order is correct
    I would like to see an itemised receipt with a grand total.

# Use the twilio-python package to implement this next one. You will need to use mocks too.

    As a customer
    So that I am reassured that my order will be delivered on time
    I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

2. Design the Class System
Consider diagramming out the classes and their relationships. Take care to focus on the details you see as important, not everything. The diagram below uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com

 ┌─────────────────────────────────────────────────────────────┐
 │ class Takeaway()                                            │
 │    self.menu = {item:cost, ...}                             │
 │    self.used_order_numbers = []                             │
 │                                                             │
 │  get_menu()                                                 │
 │    returns self.menu                                        │
 │                                                             │
 │  create_order(order_number, name)                           │
 │    creates new instance of Order class                      │
 │                                                             │
 │  print_receipt(order_number)                                │
 │   prints nicely formatted reciept                           │
 │   listing all items and grand total                         │
 │   in order                                                  │
 │                                                             │
 │  confirm_order(order_number)                                │
 │    confirms order by  SMS                                   │
 │    use twilio API                                           │
 │                                                             │
 └───────┬─▲───────────────────────────────────────────────────┘
         │ │
         │ │
  ┌──────▼─┴───────────────────────────┐
  │ class Order(order_number, name)    │
  │   self.order_number = order_number │
  │                                    │
  │   self.name = name                 │
  │                                    │
  │   self.items = {}                  │
  │                                    │
  │   self.total = int(total of values │
  │                in self.items)      │
  │                                    │
  │ add(item)                          │
  │  adds item from menu to self.items │
  │  adds cost from menu to self.total │
  └────────────────────────────────────┘

3. Create Examples as Integration Tests
Create examples of the classes being used together in different situations and combinations that reflect the ways in which the system will be used.

# EXAMPLE

"""
Given a customer name
create_order() creates an instance of Order() with self.name stored and unique order number
"""
def test_creates_order_with_name_stored()
    takeaway = Takeaway()
    order_number = generate_order_number()
    order_number.value = takeaway.create_order("Jack")
    assert jacks_order.name == "Jack"

"""
Given and order of multiple items
print_receipt() returns a nicely formatted receipt listing all items, costs and grand total
"""
def test_print_receipt_returns_correctly():
    takeaway = Takeaway()
    jacks_order = takeaway.create_order("Jack")
    jacks_order.add(takeaway.menu['chips'])
    jacks_order.add(takeaway.menu['burger'])
    assert jacks_order.print_receipt() == .....

5. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.