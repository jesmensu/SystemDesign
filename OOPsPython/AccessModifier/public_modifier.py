from protected_modifier import Geek, Student

# creating objects of the derived class        
obj = Geek("R2J", 1706256, "Information Technology") 
 
# calling public member functions of the class
obj.displayDetails() 


obj._displayRollAndBranch()
st = Student("R2I", 170600, "Information Technology")
st._displayRollAndBranch()