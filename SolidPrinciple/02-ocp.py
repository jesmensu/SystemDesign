# Open Close Principle: Open for extension but closed for modification.


# Without OCP
from math import pi
# class Shape:
#     def __init__(self, shape_type, **kwargs):
#         self.shape_type = shape_type
#         if self.shape_type == "rectangle":
#             self.width = kwargs["width"]
#             self.height = kwargs["height"]
#         elif self.shape_type == "circle":
#             self.radius = kwargs["radius"]

#     def calculate_area(self):
#         if self.shape_type == "rectangle":
#             return self.width * self.height
#         elif self.shape_type == "circle":
#             return pi * self.radius**2

# If we want to add another shape square here we have to modify the existing class 


# With OCP
from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self):
        self._pi = 3
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    # def __init__(self,radius):
    #     self.radius = radius
    def calculate_area(self, radius):
        return self._pi * radius**2

class Rectangle(Shape):
    def calculate_area(self, width, height):
        return width * height

class Square(Shape):
    def calculate_area(self, side):
        return side**2
    
c = Circle()
print(c.calculate_area(2))
