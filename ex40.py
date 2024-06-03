class Song(object):
    # Define the Song class
    
    def __init__(self, lyrics):
        # Constructor method to initialize the Song instance with lyrics
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        # Method to print each line of the song's lyrics
        for line in self.lyrics:
            print(line)
            
# Create an instance of Song with the lyrics of "Happy Birthday"
happy_bday = Song(["Happy birthday to you", 
                   "I don't want to get sued", 
                   "So I'll stop right there"])

# Create an instance of Song with the lyrics of "Bulls on Parade"
bulls_on_parade = Song(["They rally around the family",
                        "with pockets full of shells"])

# Call the sing_me_a_song method to print the lyrics of "Happy Birthday"
happy_bday.sing_me_a_song()

# Call the sing_me_a_song method to print the lyrics of "Bulls on Parade"
bulls_on_parade.sing_me_a_song()