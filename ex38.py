# Initial string containing less than 10 items
ten_things = "Apples oranges crows Telephone Light Sugar"

# Notify the user that the list doesn't have 10 items and will be fixed
print("Wait there are not 10 things in that list. Let's fix that.")

# Split the initial string into a list of words
stuff = ten_things.split(' ')  # ['Apples', 'oranges', 'crows', 'Telephone', 'Light', 'Sugar']

# Additional items to add to the list until it contains 10 items
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# Add items from more_stuff to stuff until stuff contains exactly 10 items
while len(stuff) != 10:
    # Remove the last item from more_stuff and store it in next_one
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    # Add the removed item to stuff
    stuff.append(next_one)
    # Print the current number of items in stuff
    print(f"There are {len(stuff)} items now.")

# Notify the user that the list now contains 10 items
print("There we go: ", stuff)

# Demonstrate some list operations with the stuff list
print("Let's do some things with stuff.")

# Print the second item in the list (index 1)
print(stuff[1])

# Print the last item in the list
print(stuff[-1])

# Remove and print the last item in the list
print(stuff.pop())

# Join the items in the list with a space and print the resulting string
print(' '.join(stuff))

# Join the 4th and 5th items (index 3 and 4) in the list with a '#' and print the resulting string
print('#'.join(stuff[3:5]))