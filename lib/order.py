class Order:

    def __init__(self, order_number, name):
        self.order_number = order_number
        self.name = name
        self.items = {}
        self.total = 0

    def add(self, item):
        self.items.update(item)
        self.total = sum(self.items.values())