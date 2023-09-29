class Order:

    def __init__(self, order_number, name):
        self.menu = {"Cheeseburger": 6, "Fries": 3, "Hotdog": 5, "Pizza": 8, "Fried chicken": 7, "Milkshake": 4, "Coke": 2}
        self.order_number = order_number
        self.name = name
        self.items = {}
        self.total = 0

    def get_menu(self):
        return self.menu

    def add(self, item):
        self.items.update({item:self.menu[item]})
        self.total = sum(self.items.values())

    def print_receipt(self):
        item_list = self.items
        total = self.total
        receipt = f"Order number: {self.order_number}\nCustomer name: {self.name}\n"
        for item in item_list:
            receipt += f"{item}: £{self.items[item]}" + "\n"
        receipt += f"The total cost of your order is: £{total}"
        return receipt