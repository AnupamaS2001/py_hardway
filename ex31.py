
print("""You enter a dark room with two doors.
      Do you go through door #1 or door #2?""")

# Gwaiting for user input
door = input("> ")

# If #1
if door == "1":
    #giving options to user
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    
    # waiting for input
    bear = input("> ")

    # comparing the input
    if bear == "1":
        print("The bear eats your face off.  Good job!")
    elif bear == "2":
        print("The bear eats your legs off.  Good job!")
    else:
        # if user enters something other than 1 or 2
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")
        
# Iuser input is door #2
elif door == "2":
    # options
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    
    # waiting for input
    insanity = input("> ")
    # comparing input
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
# if something else
else:
    print("You stumble around and fall on a knife and die. Good job!")