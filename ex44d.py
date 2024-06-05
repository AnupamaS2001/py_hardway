class Parent(object):
    # Method in Parent class that can be overridden
    def override(self):
        print("PARENT override()")
        
    # Method in Parent class that will be implicitly inherited
    def implicit(self):
        print("PARENT implicit()")
        
    # Method in Parent class that can be overridden and extended
    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    # Override the override method from Parent class
    def override(self):
        print("CHILD override()")
         
    # Override the altered method from Parent class
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")  
        super(Child, self).altered()  # Call Parent's altered method using super()
        print("CHILD, AFTER PARENT altered()")  

# Create an instance of Parent class
dad = Parent()

# Create an instance of Child class
son = Child()

# Call implicit method on Parent instance
dad.implicit()  # Output: PARENT implicit()

# Call implicit method on Child instance
son.implicit()  # Output: PARENT implicit()

# Call override method on Parent instance
dad.override()  # Output: PARENT override()

# Call override method on Child instance
son.override()  # Output: CHILD override()

# Call altered method on Parent instance
dad.altered()  # Output: PARENT altered()

# Call altered method on Child instance
son.altered()  
