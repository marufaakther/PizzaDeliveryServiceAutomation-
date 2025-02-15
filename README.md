# PizzaDeliveryServiceAutomation
This is a simple command-line-based Pizza Delivery Service written in Python. The project allows users to view a menu of available pizzas, place an order, and receive an order summary. The menu is dynamically loaded from a text file (menu.txt), making it easy to update without modifying the source code
Features

Load pizza menu from an external menu.txt file.

Display available pizzas with ingredients and prices.

Allow users to select multiple pizzas for an order.

Show an order summary before finalizing.

Handle incorrect inputs gracefully.

Installation & Usage

Prerequisites

Python 3.x

Steps to Run the Program

Clone this repository:

git clone https://github.com/your-username/pizza-delivery.git
cd pizza-delivery

Ensure you have a menu.txt file in the same directory with the following format:

Margherita;Tomato,Mozzarella,Basil;8.99
Pepperoni;Tomato,Mozzarella,Pepperoni;10.99
Veggie;Tomato,Mozzarella,Peppers,Onions,Olives;9.99
BBQ Chicken;BBQ Sauce,Mozzarella,Chicken,Onions;12.99

Run the script:

python pizza_delivery.py

Follow the prompts to place an order.

Future Enhancements

Add an option to remove items from the order.

Implement order history logging.

Introduce online payment integration.

Contributions

Contributions are welcome! Feel free to fork the repository and submit a pull request with your improvements.

License

This project is open-source and available under the MIT License.

