#initialising list with numbers
the_count = [1, 2, 3, 4, 5]

# Initializsing list with strings
fruits = ['apples', 'oranges', 'pears', 'apricots']

# Initialize a list with numbers and strings
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# Looping through 'the_count' list and print number
for number in the_count:
    print(f"This is count {number}")

# Looping through the string list and print each string
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# Looping through the change list and printing items
for i in change:
    print(f"I got {i}")

# empty list to store elements
elements = []

# Loop from 0 to 5 and add each number to the elements
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)

# Loop through the elemtents and prnint items
for i in elements:
    print(f"Element was: {i}")