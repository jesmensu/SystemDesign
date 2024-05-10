"""
Learn how to create simple factory which helps to hide
logic of creating objects.
"""
# ================== Simple Factory ====================
from abc import ABCMeta, abstractmethod

class Person(metaclass=ABCMeta):
    @abstractmethod
    def create(self):
        pass

class HR(Person):
    def create(self, name):
        print(f"HR {name} is created")

class Engineer(Person):
    def create(self, name):
        print(f"Engineer {name} is created")

class PersonFactory(object):
    @staticmethod
    def createPerson(designation, name):
        eval(designation)().create(name)

# if __name__ == "__main__":
#     designation = input("Please enter the designation - ")
#     name = input("Please enter the person's name - ")
#     PersonFactory.createPerson(designation, name)


# ===================== Factory Method Pattern =====================
from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def read(self):
        pass
    @abstractmethod
    def write(self):
        pass

class TextDocument(Document):
    def read(self):
        print("Reading text document")
    def write(self):
        print("Writing text document")

class SpreadsheetDocument(Document):
    def read(self):
        print("Reading spreadsheet document")
    def write(self):
        print("Writing spreadsheet document")

class DocumentCreator(ABC):
    @abstractmethod
    def create_document(self):
        pass

class TextDocumentCreator(DocumentCreator):
    def create_document(self):
        print("Created text document")
        return TextDocument()

class SpreadsheetDocumentCreator(DocumentCreator):
    def create_document(self):
        print("Created spreadsheet document")
        return SpreadsheetDocument()
    
if __name__ == "__main__":
    textDocumentCreator = TextDocumentCreator()
    textDocument = textDocumentCreator.create_document()
    textDocument.read()
    textDocument.write()

    spreadsheetDocumentCreator = SpreadsheetDocumentCreator()
    spreadsheetDocument = spreadsheetDocumentCreator.create_document()
    spreadsheetDocument.read()
    spreadsheetDocument.write()


# ======================= Factory Abstract Method =========================
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing Circle")

class Square(Shape):
    def draw(self):
        print("Drawing Square")

class ShapeFactory(ABC):
    @abstractmethod
    def create_shape(self, shape_type):
        pass

class CircleFactory(ShapeFactory):
    def create_shape(self, shape_type):
        if shape_type.upper() == "CIRCLE":
            return Circle()
        return None  # Handle invalid shape type or raise an exception

class SquareFactory(ShapeFactory):
    def create_shape(self, shape_type):
        if shape_type.upper() == "SQUARE":
            return Square()
        return None  # Handle invalid shape type or raise an exception

if __name__ == "__main__":
    shape_factory = CircleFactory()
    circle = shape_factory.create_shape("CIRCLE")
    circle.draw() 

    shape_factory = SquareFactory()
    square = shape_factory.create_shape("SQUARE")
    square.draw()

