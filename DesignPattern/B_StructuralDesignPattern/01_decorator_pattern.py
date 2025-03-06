# Component interface
class Coffee:
    def cost(self):
        pass

# Concrete component
class SimpleCoffee(Coffee):
    def cost(self):
        return 5  # Base price of simple coffee

# Decorator abstract class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

# Concrete decorators
class Milk(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2  # Additional cost of milk

class Sugar(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1  # Additional cost of sugar

class Vanilla(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 3  # Additional cost of vanilla flavor

# Client code
simple_coffee = SimpleCoffee()
print("Cost of simple coffee:", simple_coffee.cost())

# Add milk to the simple coffee
milk_coffee = Milk(simple_coffee)
print("Cost of coffee with milk:", milk_coffee.cost())

# Add sugar to the coffee with milk
sugar_milk_coffee = Sugar(milk_coffee)
print("Cost of coffee with milk and sugar:", sugar_milk_coffee.cost())

# Add vanilla flavor to the coffee with milk and sugar
vanilla_sugar_milk_coffee = Vanilla(sugar_milk_coffee)
print("Cost of coffee with milk, sugar, and vanilla:", vanilla_sugar_milk_coffee.cost())
