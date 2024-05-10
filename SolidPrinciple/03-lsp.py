#  Liskov Substitute Principle
# Subclass should extend the capability of parent class but not narrow it down
# Where the parent class is using, it should be posible to substitute the parrent class with the child class
# If we extend list to create the stack or queue, it violates the LSP since we have narowed down some functionalities of list 
# in the stack or queue implementation we have to narrow down some functionalities of list.
# We can not substitute the list with stack or queue

# Violating LSP
class Shape:
    def draw(self):
        print("Shape has drawn")
    def rotate(self):
        print("Shape has rotated")

class circle(Shape):
    def rotate(self):
        raise ReferenceError("The functionality is not applicable for circle")
    

# Here rotate function has narowed down for circle. We can't use circle class object in place of Shape class.
# We can use Interface Segrigation Principle to solve the issue

# Applying LSP
class Drawable:
    def draw(self):
        print("Shape has drawn")
class Rotatable:
    def rotate(self):
        print("Shape has rotated")

class circle(Drawable):
    def draw(self):
        print("circle has drawn")
class Rectangle(Drawable,Rotatable):
    def draw(self):
        print("Rectangle has drawn")
    def rotate(self):
        print("Rectangle has rotated")


# Using Abstraction
from abc import ABC, abstractmethod
class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass
class Rotatable(ABC):
    @abstractmethod
    def rotate(self):
        pass

class circle(Drawable):
    def draw(self):
        print("circle has drawn")
class Rectangle(Drawable,Rotatable):
    def draw(self):
        print("Rectangle has drawn")
    def rotate(self):
        print("Rectangle has rotated")

