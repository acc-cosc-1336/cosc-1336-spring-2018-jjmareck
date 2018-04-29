from src.homework.homework10.player import Player
from src.homework.homework10.game_log import GameLog

#write import statement for GameLog class


#Create a game log instance
game_log = GameLog()
#SEnd the game_log instance to Player class as an argument
Player(game_log).roll_doubles()


#call the game log display method below

game_log.display_log()
