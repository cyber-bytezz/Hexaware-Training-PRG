from typing import Any

class Customer:
    def __init__(self, customer_id: int, name: str, address: str):
        self.__customer_id = customer_id
        self.__Customer__name = name
        self.__Customer__address = address

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)

    def __str__(self) -> str:
        return f"Customer(id={self.__customer_id}, name={self.__Customer__name}, address={self.__Customer__address})"

customer_obj1 = Customer(100, "null", "Second Street, Link Road, Chennai") 

print(customer_obj1)

print("Name:", customer_obj1.__getattribute__("_Customer__name"))
print("ID:", customer_obj1.__getattribute__("_Customer__customer_id"))
print("Address:", customer_obj1.__getattribute__("_Customer__address"))

customer_obj1.__setattr__("_Customer__name", "None")

print(customer_obj1)
