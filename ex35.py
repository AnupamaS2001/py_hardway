from sys import exit

def gold_room():
    """
    This function simulates a room full of gold.
    The player must choose how much gold to take.
    """
    print("This room is full of gold. How much do you take?")
    
    choice = input("> ")
    
    # Check if the input contains '0' or '1' to ensure it's a number
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")
        
    # Determine if the player is greedy or not based on the amount of gold taken
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)  # Exit the game with a success status
    else:
        dead("You greedy bastard!")  # End the game with a message

def bear_room():
    """
    This function simulates a room with a bear.
    The player must figure out how to move the bear to access another door.
    """
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    
    bear_moved = False  # Flag to check if the bear has moved
    while True:
        choice = input("> ")
        
        # Different actions based on the player's choice
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True  # Update the flag as the bear has moved
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()  # Move to the gold room if the bear has moved
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    """
    This function simulates a room with the mythical creature Cthulhu.
    The player must choose between fleeing or eating their head.
    """
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    
    choice = input("> ")
    
    # Actions based on the player's choice
    if "flee" in choice:
        start()  # Restart the game
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()  # Stay in the Cthulhu room

def dead(why):
    """
    This function handles the player's death.
    It prints a message and exits the game.
    """
    print(why, "Good job!")
    exit(0)  # Exit the game with a failure status

def start():
    """
    This function starts the game.
    The player chooses between two doors.
    """
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    
    choice = input("> ")
    
    # Direct the player to the appropriate room based on their choice
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

# Start the game
start()