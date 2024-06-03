#setting a value for 1 
i = 0

# empty list to store the values
numbers = []

# while loop will execute till the value of i < 6
while i < 6: 
    print(f"At the top i is {i}")
    
    # Appending the value of i to list created 
    numbers.append(i)
    
    # Increment the value of i by 1
    i = i + 1
   
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")
    

print("The numbers: ")

# printing each value in numbers list using for loop
for num in numbers:
    
    print(num)