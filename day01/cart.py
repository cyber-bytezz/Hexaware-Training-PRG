class Product:
    
    def __init__(self, name, price, quantity):
        self.name, self.price, self.quantity = name, price, quantity

    def __str__(self):
        return f"{self.name} - ₹{self.price:.2f} x {self.quantity}"


class ShoppingCart:
    
    def __init__(self):
        self.cart = {}

    def add_product(self):
        name = input("Enter product name: ").strip()
        if not name: return print("Product name cannot be empty.")
        
        price = self.get_valid_input("Enter product price (₹): ", float)
        quantity = self.get_valid_input("Enter product quantity: ", int)

        if name in self.cart:
            self.cart[name].quantity += quantity
        else:
            self.cart[name] = Product(name, price, quantity)
        print(f"Added {name} to cart.")

    def remove_product(self):
        if not self.cart: return print("Cart is empty.")
        name = input("Enter product name to remove: ").strip()
        print(f"Removed {name}") if self.cart.pop(name, None) else print(f"{name} not in cart.")

    def update_quantity(self):
        if not self.cart: return print("Cart is empty.")
        name = input("Enter product name to update: ").strip()
        if name in self.cart:
            self.cart[name].quantity = self.get_valid_input("Enter new quantity: ", int)
            print(f"Updated {name}.")
        else:
            print(f"{name} not in cart.")

    def view_cart(self):
        if not self.cart: return print("Cart is empty.")
        print("\nShopping Cart:")
        for item in self.cart.values(): print(f"  {item}")

    def calculate_total(self):
        total = sum(p.price * p.quantity for p in self.cart.values())
        print(f"\nTotal Price: ₹{total:.2f}")

    @staticmethod
    def get_valid_input(prompt, dtype):
        while True:
            try:
                value = dtype(input(prompt))
                if value > 0: return value
                print("Enter a positive value.")
            except ValueError:
                print("Invalid input. Try again.")

                
def main():
    cart = ShoppingCart()
    actions = {
        "1": cart.add_product, "2": cart.remove_product,
        "3": cart.update_quantity, "4": cart.view_cart,
        "5": cart.calculate_total, "6": exit
    }

    while True:
        print("\nShopping Cart Menu\n1. Add Product\n2. Remove Product\n3. Update Quantity\n4. View Cart\n5. Calculate Total\n6. Exit")
        actions.get(input("Choose an option: ").strip(), lambda: print("Invalid choice."))()


if __name__ == "__main__":
    main()
