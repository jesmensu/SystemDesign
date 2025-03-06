import copy

# Prototype interface
class ShapePrototype:
    def clone(self):
        pass

# Concrete Prototype
class Circle(ShapePrototype):
    def __init__(self, radius):
        self.radius = radius

    def clone(self):
        return copy.deepcopy(self)

# Client code
circle_prototype = Circle(5)
circle_copy = circle_prototype.clone()
print(circle_copy.radius)  # Output: 5


# Partial Copying
class Prototype:
    def __init__(self, param1, param2, param3):
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        ...

    def clone(self, param1, param2):
        # Create a shallow copy of self
        clone = copy.copy(self)
        # Customize the clone by assigning only required parameters
        clone.param1 = param1
        clone.param2 = param2
        # Don't assign param3 and subsequent parameters
        return clone
    
clone_prototype = Prototype(2,3,4)
c = clone_prototype.clone(6,7)

#Parameterised cloning
class Prototype:
    def __init__(self, param1, param2, param3):
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        ...

    def clone(self, param1=True, param2=True, param3=True):
        # Create a shallow copy of self
        clone = copy.copy(self)
        # Customize the clone by conditionally assigning parameters
        if not param1:
            clone.param1 = None
        if not param2:
            clone.param2 = None
        if not param3:
            clone.param3 = None
        return clone
clone_prototype = Prototype(2,3,4)
c = clone_prototype.clone(param1 = False)
print(c.__dict__)


# Using Builder
class PrototypeBuilder:
    def __init__(self):
        self.param1 = None
        self.param2 = None
        self.param3 = None
        ...

    def set_param1(self, value):
        self.param1 = value
        return self

    def set_param2(self, value):
        self.param2 = value
        return self

    def set_param3(self, value):
        self.param3 = value
        return self

    def build(self):
        return Prototype(self.param1, self.param2, self.param3, ...)

