# program to illustrate protected access modifier in a class
 
# super class
class Student:
    
     # protected data members
     _name = None
     _roll = None
     _branch = None
    
     # constructor
     def __init__(self, name, roll, branch):  
          self._name = name
          self._roll = roll
          self._branch = branch
    
     # protected member function   
     def _displayRollAndBranch(self):
          print("Roll: ", self._roll)
          print("Branch: ", self._branch)
 
 
# derived class
class Geek(Student):
 
       # constructor 
       def __init__(self, name, roll, branch): 
               #  Student.__init__(self, name, roll, branch) 
                super().__init__(name, roll, branch)
         
       # public member function 
       def displayDetails(self):
                 # accessing protected data members of super class 
                print("Name: ", self._name)   
                 # accessing protected member functions of super class 
                self._displayRollAndBranch()

class Geeks:
     def display(self):
          s = Student("R2J", 1706256, "Information Technology")
          print("inside the Geeks", s._name)
 
# creating objects of the derived class        
obj = Geek("R2J", 1706256, "Information Technology") 
 
# calling public member functions of the class
obj.displayDetails() 


obj._displayRollAndBranch()
st = Student("R2I", 170600, "Information Technology")
st._displayRollAndBranch()
g = Geeks()
g.display()