# Coffee Shop Project

## Overview

This project is a coffee shop application where we manage customers, coffees, and orders. The application models the relationships between these entities and provides functionality to interact with them.

## Project Structure

- **`customer.py`**: Contains the `Customer` class, which models a customer in the coffee shop.
- **`coffee.py`**: Contains the `Coffee` class, which represents different types of coffee available in the shop.
- **`order.py`**: Contains the `Order` class, which links customers with coffees and tracks the price of each order.
- **`tests/`**: Contains unit tests for the `Customer`, `Coffee`, and `Order` classes.

## Classes

### `Customer`
- **Attributes**:
  - `name`: The name of the customer.
- **Methods**:
  - `orders()`: Returns a list of orders associated with the customer.
  - `coffees()`: Returns a list of unique coffees ordered by the customer.
  - `create_order(coffee, price)`: Creates a new order for the customer.
  - `most_aficionado(coffee)`: Class method to find the customer who spent the most on a given coffee.

### `Coffee`
- **Attributes**:
  - `name`: The name of the coffee.
- **Methods**:
  - `orders()`: Returns a list of orders associated with the coffee.
  - `customers()`: Returns a list of unique customers who ordered the coffee.
  - `num_orders()`: Returns the total number of times the coffee has been ordered.
  - `average_price()`: Returns the average price of the coffee based on its orders.

### `Order`
- **Attributes**:
  - `customer`: The customer who made the order.
  - `coffee`: The coffee that was ordered.
  - `price`: The price of the order.
- **Methods**:
  - None (all functionality is provided through properties and initialization).

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd your-repository
    ```

3. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application**:
    You can run your scripts directly or use a Python interpreter to interact with the classes.

2. **Run tests**:
    ```bash
    pytest
    ```

## Contributing

If you want to contribute to this project, please follow these steps:

1. **Fork the repository**.
2. **Create a new branch** (`git checkout -b feature-branch`).
3. **Make your changes**.
4. **Commit your changes** (`git commit -am 'Add new feature'`).
5. **Push to the branch** (`git push origin feature-branch`).
6. **Create a new Pull Request**.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to contact [your-email@example.com](mailto:your-email@example.com).
