## Coupling
    Coupling is a measure of how dependent two or more software modules are on each other. It describes how closely they are interconnected and how changes in one module can affect others.

## Cohesion
    Cohesion measures how closely the elements within a single module are related to each other. It reflects how well they work together to achieve a single purpose.

## Strive for low coupling and high cohesion: 
    This leads to more maintainable, reusable, and testable code. Minimize dependencies between modules/Class/functions: Use interfaces, dependency injection, and messaging for loose coupling. Group related elements within modules/Class/Function: Ensure elements within a module/class/function work cohesively towards a common goal.

## dependency injection:
    Dependency injection is a principle that helps to decrease coupling and increase cohesion.
    In Dependency injection if any class B is dependent on class A, instead of creating object inside the class B, we can inject the object through the constructor of class B.
    