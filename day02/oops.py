class Customer:
    def __init__(self, customer_id: int, name: str, address: str):
        """Initialize private attributes"""
        self.__customer_id = customer_id
        self.__name = name
        self.__address = address

    # Getter and setter for customer_id
    def get_customer_id(self):
        return self.__customer_id

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    # Getter and setter for name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # Getter and setter for address
    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def __str__(self):
        return f"[Name: {self.__name}, Customer ID: {self.__customer_id}, Address: {self.__address}]"

if __name__ == "__main__":

    customer_obj1 = Customer(100, "Saheer", "Second Street, Link Road, Chennai")

    print(customer_obj1)

    # Updating values
    customer_obj1.set_name("John Doe")
    customer_obj1.set_address("123 Main St, Bangalore")

    # Printing updated values
    print(f"Updated Name: {customer_obj1.get_name()}")
    print(f"Updated Address: {customer_obj1.get_address()}")

    # Printing the final object state
    print(customer_obj1)
