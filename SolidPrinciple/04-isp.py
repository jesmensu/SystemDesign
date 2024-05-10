# Interface segregation principle
# Clients should not be forced to depend upon interface that they do not use
# Don’t show your clients more than they need to see.
# ISP complements(gives feature) other SOLID principles like Single Responsibility Principle (SRP) and Liskov Substitution Principle (LSP). 
# Violates ISP:
#   + Robot is forced to implement eat() and sleep() even though it doesn't need them, violating ISP.
#   + This creates unnecessary coupling and potential for errors.
from abc import ABC, abstractmethod
class Worker(ABC):
    @abstractmethod
    def work(self):
        pass
    def eat(self):
        pass
    def sleep(self):
        pass

class Human(Worker):
    def work(self):
        print("abstract method")

class Robot(Worker):
    #  ... implements work() but not eat() or sleep()
    pass

h = Human()
h.eat()
# Fix ISP:
#   + Interfaces are now segregated based on functionality.
#   + Robot only implements the methods it needs, reducing coupling.
#   + Code becomes more flexible and maintainable.

class Workable:
    def work():
        pass

class Feedable:
    def eat():
        pass

class Restful:
    def sleep():
        pass

class Human(Workable, Feedable, Restful):
    #  ... implements all methods
    pass

class Robot(Workable):
    # ... implements only work()
    pass





# Violates the ISP
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

    def fax(self, document):
        raise NotImplementedError("Fax functionality not supported")

    def scan(self, document):
        raise NotImplementedError("Scan functionality not supported")

class ModernPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")


# This implementation violates the ISP because 
# it forces OldPrinter to expose an interface that the class doesn’t implement or need. 
# To fix this issue, you should separate the interfaces into smaller and more specific classes. 
# Then you can create concrete classes by inheriting from multiple interface classes as needed.

# printers_isp.py

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

class NewPrinter(Printer, Fax, Scanner):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")