#write import statements for Player and Die class
from src.homework.homework9.player import Player
from src.homework.homework9.die import Die
#Create an instance of the Main class and call/execute the roll_doubles method

class Main:
    def __init__(self):
        self.player = Player()
        self.player.roll_doubles()

main = Main()
