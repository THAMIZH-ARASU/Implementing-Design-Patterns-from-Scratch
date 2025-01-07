from abc import ABC, abstractmethod

#1. Define the Product interface
class Coffee(ABC):
    @abstractmethod
    def prepare(self):
        pass

#2. Implement the Concrete Products
class Espresso(Coffee):
    def prepare(self):
        return "Preparing a rich and strong Espresso"
    
class Cappuccino(Coffee):
    def prepare(self):
        return "Preparing a creamy Cappuccino"

class Latte(Coffee):
    def prepare(self):
        return "Preparing a smooth and silky Latte"

#3. Implement the Factory
class CoffeeMachine:
    def make_coffee(self, coffee_type: str) -> Coffee:
        if coffee_type == "Espresso":
            return Espresso().prepare()
        elif coffee_type == "Cappuccino":
            return Cappuccino().prepare()
        elif coffee_type == "Latte":
            return Latte().prepare()
        else:
            return "Unknown coffee type!"

#4. Use the Factory to Create Products
if __name__ == "__main__":
    coffee_machine = CoffeeMachine()
    
    print(coffee_machine.make_coffee("Espresso"))
    print(coffee_machine.make_coffee("Cappuccino"))
    print(coffee_machine.make_coffee("Latte"))
    print(coffee_machine.make_coffee("Mocha"))