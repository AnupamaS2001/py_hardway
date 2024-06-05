class Parent(object):
    # Define a method called implicit in the Parent class
    def implicit(self):
        print("PARENT implicit()")
        
# Create a Child class that inherits from Parent
class Child(Parent):
    pass  # The Child class does not override any methods from Parent

# Create an instance of the Parent class
dad = Parent()

# Create an instance of the Child class
son = Child()

# Call the implicit method on the Parent instance
dad.implicit()

# Call the implicit method on the Child instance
# Since Child does not override the implicit method, it inherits the method from Parent
son.implicit()