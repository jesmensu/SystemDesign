class Car:
    def __init__(self):
        self.model = None
        self.color = None
        self.year = None

    def set_model(self, model):
        self.model = model
        return self  # Returning self allows chaining

    def set_color(self, color):
        self.color = color
        return self

    def set_year(self, year):
        self.year = year
        return self

    def display(self):
        print(f"Car: {self.model}, Color: {self.color}, Year: {self.year}")

# Usage
car = Car().set_model("Tesla Model 3").set_color("Blue").set_year(2023)
car.display()
