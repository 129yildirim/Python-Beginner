class Parent:

    def print_last_name(self):
        print('Roberts')
    

# We can define the parent(super class) of the class inside the parantheses
class Child(Parent):

    def print_first_name(self):
        print("myFirrstName")

    def print_last_name(self):
        print("Yildiirim")


child1 = Child()
child1.print_first_name()
child1.print_last_name()