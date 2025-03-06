# A. Creational Design Patterns
    Creational design patterns focus on object creation mechanisms, improving flexibility and reusability while hiding complex instantiation logic.
## 1. Singleton Pattern
    The Singleton design pattern ensures a class has only one instance and provides
    a global access point to it. This means we control object creation and guarantee
    there’s only ever a single instance throughout the application.
#### Eager Initialization:
    This approach creates the instance as soon as the class is loaded. It’s simple but
    may waste resources if the object isn’t used immediately.
#### Lazy Initialization:
    The instance is created only when it’s first requested. 
#### Synchronized Lazy Initialization:
    The Singleton instance is created only when it’s requested for the first time. It uses
    a synchronized method to ensure thread safety.
    The synchronization can introduce performance overhead.
#### Double checked locking:
    This is thread safe and provide bettern performance than previous solution

## 2. Factory Design pattern
    Used to create concrete implementations of a common interface. Used when object creation and business logic we need to keep at one place.
    The Simple Factory pattern, also known as the Static Factory pattern. It encapsulates the object creation logic within a separate factory class.
    Factory Method pattern focuses on creating a single object, allowing subclasses to provide the specific implementation.
    Abstract Factory pattern focuses on creating families of related objects, providing an interface to create multiple related objects.
    Factory Design Pattern creates a single product at a time.
    Abstract Factory Design Pattern creates families of related products.
## 3. Builder Pattern
    Builder Method is a Creation Design Pattern which aims to construct object using construction and through setter function.Using the same construction code, we can produce different types and representations of the object easily. A separate builder class is used to create the object. The object is not created until the build() method is called. 
    Constructed object is immutable.

## 4. Cascading Pattern
    Used to modify an object’s attributes using method chaining, usually within the same class.
    Similarity with Builder pattern. But Builder class and build() method is not used. Constructed object is mutable.

## 5. Prototype Pattern
     It involves cloning an existing object rather than creating a new one from scratch. This pattern is useful when the construction of a new object is more efficient by copying an existing object.
     The client code retrieves an existing prototype and calls its clone method to create a new object.
     If cloned object requires only a subset of the parameters from the original object, options to handle it within the Prototype Design Pattern:
     1. Partial Copying
     2. Parameterized Cloning
     3. Use a Builder
#### Adv:
    Flexibility: Allows adding or removing objects at runtime.
    Performance: Avoids expensive object creation operations by cloning existing objects.
    Simplicity: Simplifies object creation by providing a mechanism for copying existing objects.
    The Prototype Design Pattern promotes code reusability and reduces the complexity of object creation by allowing objects to be cloned from existing prototypes.


# B. Structural Design Pattern:
    Combine or arrange different classes and objects to form a complex or bigger structure to solve a particular requirement.
## Decorator Pattern
    This pattern helps to add more functionalities to the existing object without changing its structure.
    It involves wrapping objects with decorators that add new functionality while preserving their original interface.
## Proxy Pattern
    Helps to provide control access to the original object. It acts as an intermediary or a wrapper around the real object, allowing the proxy to add additional functionality, such as caching, logging, or access control, without changing the original object's code.

    The Proxy receives the client's requests and can perform additional tasks before or after forwarding the requests to the Real Subject. The Real Subject performs the actual work requested by the client, and the result is returned to the Proxy. The Proxy then returns the result to the client.

## Adapter Pattern
    Design pattern that allows objects with incompatible interfaces to work together converting the interface of a class into another interface that a client expects. 
## Bridge Pattern
    It involves creating two separate class hierarchies: one for the abstraction and another for the implementation. The bridge pattern provides a bridge between these two hierarchies, enabling them to evolve independently.
## Composite Pattern
    This pattenr helps in scenarios where we have object inside object (tree like structure)

## Facade Pattern
    Helps to hide the system details or complexity from the client. It acts as a single entry point to a set of interfaces in a subsystem, providing a higher-level interface that makes the subsystem easier to use.
## Flyweight Pattern


# C. Behavioural Design patterns
## Strategy Design Pattern
    Helps to define multiple algorithm for the task and we can select any algorithm depending on the situation.
## Observer Design Pattern
## Chain of Responsibility Design Pattern
    Allows multiple request along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.
    It includes a method for setting the next handler in the chain and a method for handling requests.
## Command Design Pattern
## State Design Pattern
    Allows an object to alter its behaviour when its internal state changes.
## Interprete Design Pattern
## Command Design Pattern
## Template Method Pattern
## Memento design pattern
## Visitor Design Pattern



