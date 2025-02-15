import time


class Pizza:
    def __init__(self, name, ingredients, price):
        self.name = name
        self.ingredients = ingredients
        self.price = float(price)

    def __str__(self):
        return f"{self.name} Pizza - Ingredients: {', '.join(self.ingredients)} - Price: ${self.price:.2f}"


class Order:
    def __init__(self, customer_name, address):
        self.customer_name = customer_name
        self.address = address
        self.pizzas = []
        self.total_price = 0.0

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)
        self.total_price += pizza.price

    def __str__(self):
        pizzas_list = '\n'.join([str(pizza) for pizza in self.pizzas])
        return (f"Order for {self.customer_name}\n"
                f"Address: {self.address}\n"
                f"Pizzas:\n{pizzas_list}\n"
                f"Total Price: ${self.total_price:.2f}")


class PizzaDeliveryService:
    def __init__(self, menu_file):
        self.menu = self.load_menu(menu_file)

    def load_menu(self, menu_file):
        menu = []
        try:
            with open(menu_file, 'r') as file:
                for line in file:
                    parts = line.strip().split(';')  # Expecting format: Name;Ingredient1,Ingredient2;Price
                    if len(parts) == 3:
                        name = parts[0]
                        ingredients = parts[1].split(',')
                        price = parts[2]
                        menu.append(Pizza(name, ingredients, price))
        except FileNotFoundError:
            print("Error: Menu file not found!")
        return menu

    def display_menu(self):
        print("\n--- Menu ---")
        for i, pizza in enumerate(self.menu, start=1):
            print(f"{i}. {pizza}")

    def take_order(self):
        customer_name = input("Enter your name: ")
        address = input("Enter your delivery address: ")
        order = Order(customer_name, address)

        while True:
            self.display_menu()
            choice = input("Select a pizza by number (or type 'done' to finish): ")

            if choice.lower() == 'done':
                break

            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(self.menu):
                    pizza = self.menu[choice - 1]
                    order.add_pizza(pizza)
                    print(f"Added {pizza.name} to your order.")
                else:
                    print("Invalid choice. Please select a valid pizza number.")
            else:
                print("Invalid input. Please enter a number or 'done'.")

        print("\n--- Order Summary ---")
        print(order)
        print("\nThank you for your order! Your pizza will be delivered soon.")


if __name__ == "__main__":
    print("Welcome to the Pizza Delivery Service!")
    service = PizzaDeliveryService("menu.txt")  # Load menu from file
    service.take_order()
