class Customer:
    _all = []

    def __init__(self, name):
        # Add name to the list of customers when initialized
        self.set_name(name)
        Customer._all.append(self)

    def set_name(self, value):
        # Check if name is a string and length between 1 and 15
        if type(value) == str:
            if len(value) >= 1 and len(value) <= 15:
                self._name = value
            else:
                raise Exception("Name must be between 1 and 15 characters.")
        else:
            raise Exception("Name must be a string.")

    def get_name(self):
        # Get name of the customer
        return self._name

    name = property(get_name, set_name)

    def orders(self):
        # Find all orders for this customer
        customer_orders = []
        for order in Order._all:
            if order.customer == self:
                customer_orders.append(order)
        return customer_orders

    def coffees(self):
        # Get unique coffees this customer ordered
        coffee_list = []
        for order in self.orders():
            if order.coffee not in coffee_list:
                coffee_list.append(order.coffee)
        return coffee_list

    def create_order(self, coffee, price):
        # Create and return a new order
        new_order = Order(self, coffee, price)
        return new_order

    @classmethod
    def most_aficionado(cls, coffee):
        # Find customer who spent the most on a specific coffee
        customer_spending = {}
        for order in Order._all:
            if order.coffee == coffee:
                if order.customer not in customer_spending:
                    customer_spending[order.customer] = order.price
                else:
                    customer_spending[order.customer] += order.price

        if customer_spending:
            highest_spender = max(customer_spending, key=customer_spending.get)
            return highest_spender
        else:
            return None
