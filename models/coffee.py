# coffee.py
class Coffee:
    _all = []

    def __init__(self, name):
        self.name = name
        Coffee._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not hasattr(self, '_name'):
            if isinstance(value, str) and len(value) >= 3:
                self._name = value
            else:
                raise ValueError("Name must be a string with at least 3 characters.")
        else:
            raise AttributeError("Name cannot be changed once set.")
    
    def orders(self):
        return [order for order in Order._all if order.coffee == self]
    
    def customers(self):
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        orders = self.orders()
        if orders:
            return sum(order.price for order in orders) / len(orders)
        return 0

