class Parent(object):
    # Define a method called altered in the Parent class
    def altered(self):
        print("PARENT altered")

class Child(Parent):
    # Override the altered method in the Child class
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")  # Print a message before calling the Parent's altered method
        super(Child, self).altered()  # Call the altered method from the Parent class
        print("CHILD, AFTER PARENT altered()")  # Print a message after calling the Parent's altered method

# Create an instance of the Parent class
dad = Parent()

# Create an instance of the Child class
son = Child()

# Call the altered method on the Parent instance
dad.altered()

#Call the altered method on the Child instance
son.altered()