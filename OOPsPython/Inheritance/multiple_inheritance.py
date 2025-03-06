
class A:
    def do_thing(self):
        print('From A')

class B(A):
    def do_thing(self):
        print('From B')

class C(A):
    def do_thing(self):
        print('From C')

class D(B, C):
    pass

d = D()
d.do_thing()


# when two classes have a common ancestor, and if another class is the derived class of this two class, 
# then diamond problem arise in some languages because of ambiguation of method call 
# But python doesnot have this problem, because of the method resolution order. 
# In the above case we have specified D(B, C), where B.do_thing is called before C.do_thing.
# inconsistent chain is not allowed 