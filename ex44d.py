#create a class parent that is-a object
class Parent(object):
    def override(self):
        print("PARENT override()")
    def implicit(self):
        print("PARENT implicit()")
    def altered(self):
        print("PARENT altered()")

#create a class child that has-a parent 
class Child(Parent):
    def override(self): #override the override function
        print("CHILD override")
    def altered(self): #alter the altered fuction
        print("CHILD, BEFORE PARENT altered(") #first override
        super(Child, self).altered() #then call the original version
        print("CHILD, AFTER PARENT altered ()") #then override again

#create an object parent
dad = Parent()
#create an object child
son = Child()

#from dad call function implicit
dad.implicit()
son.implicit() #the son inherits implicit from the dad

#from the objects call function override
dad.override()
son.override()

dad.altered()
son.altered()
