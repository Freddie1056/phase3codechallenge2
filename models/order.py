class Order:
    _all = []

    def __init__(self, customer, coffee, price):
        # Assign customer, coffee, and price when initializing the order
        self.set_customer(customer)
        self.set_coffee(coffee)
        self.set_price(price)
        Order._all.append(self)

    def set_price(self, value):
        # Set the price, ensuring it's a float between 1.0 and 10.0
        if type(value) == int or type(value) == float:
            if value >= 1.0 and value <= 10.0:
                self._price = value
            else:
                raise Exception("Price must be between 1.0 and 10.0.")
        else:
            raise Exception("Price must be a number.")

    def get_price(self):
        # Get the price of the order
        return self._price

    price = property(get_price, set_price)

    def set_customer(self, value):
        # Set the customer, ensuring it's an instance of Customer
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise Exception("Customer must be an instance of the Customer class.")

    def get_customer(self):
        # Get the customer for the order
        return self._customer

    customer = property(get_customer, set_customer)

    def set_coffee(self, value):
        # Set the coffee, ensuring it's an instance of Coffee
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            raise Exception("Coffee must be an instance of the Coffee class.")

    def get_coffee(self):
        # Get the coffee for the order
        return self._coffee

    coffee = property(get_coffee, set_coffee)
