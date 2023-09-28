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

 ┌────────────────────────────────────────┐
 │ class Takeaway()                       │
 │    self.menu = {item:cost, ...}        │
 │    self.order_history = []             │
 │                                        │
 │  generate_order_number()               │
 │    generates unique order number for   │
 │    instance of create_order            │
 │                                        │
 │  get_menu()                            │
 │    returns self.menu                   │
 │                                        │
 │  create_order(order_number, name)      │
 │    creates new instance of Order class │
 │                                        │
 │  print_receipt(order_number)           │
 │   prints nicely formatted reciept      │
 │   listing all items and grand total    │
 │   in order                             │
 │                                        │
 │  confirm_order(order_number)           │
 │    confirms order by  SMS              │
 │    use twilio API                      │
 │                                        │
 └───────┬─▲──────────────────────────────┘
         │ │
  ┌──────▼─┴───────────────────────────┐
  │ class Order(name)                  │
  │   self.order_number = str          │
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
  │                                    │
  │                                    │
  │                                    │
  │                                    │
  │                                    │
  └────────────────────────────────────┘

Also design the interface of each class in more detail.



3. Create Examples as Integration Tests
Create examples of the classes being used together in different situations and combinations that reflect the ways in which the system will be used.

# EXAMPLE

"""
Given a library
When we add two tracks
We see those tracks reflected in the tracks list
"""
library = MusicLibrary()
track_1 = Track("Carte Blanche", "Veracocha")
track_2 = Track("Synaesthesia", "The Thrillseekers")
library.add(track_1)
library.add(track_2)
library.tracks # => [track_1, track_2]
4. Create Examples as Unit Tests
Create examples, where appropriate, of the behaviour of each relevant class at a more granular level of detail.

# EXAMPLE

"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"
Encode each example as a test. You can add to the above list as you go.

5. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.