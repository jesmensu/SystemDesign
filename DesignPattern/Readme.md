# Creational Design Patterns
## Singleton Pattern
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

## Factory Design pattern
    Used to create concrete implementations of a common interface.
    The Simple Factory pattern, also known as the Static Factory pattern. It encapsulates the object creation logic within a separate factory class.
    Factory Method pattern focuses on creating a single object, allowing subclasses to provide the specific implementation.
    Abstract Factory pattern focuses on creating families of related objects, providing an interface to create multiple related objects.
    Factory Design Pattern creates a single product at a time.
    Abstract Factory Design Pattern creates families of related products.
## Builder Pattern
## Cascading Pattern
## Prototype Pattern
## Adapter Pattern

# Behavioural Design patterns
## Strategy Design Pattern
## Observer Design Pattern
## Chain of Responsibility Design Pattern
## Command Design Pattern
## State Design Pattern
## Herman 



