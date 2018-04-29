#write import statement for Die class
from src.homework.homework10.die import Die
from src.homework.homework10.score_entry import ScoreEntry


'''
Create a Player class.
Add a constructor method to create two Die attributes die1 and die2 
Add a roll_doubles method that will iterate, roll die1 and die2, display rolled values, 
and continue iterating until a double is rolled.
'''

class Player:

    def __init__(self, game_log):
        self.die1 = Die()
        self.die2 = Die()
        self.game_log = game_log

    def roll_doubles(self):
        rolled_double = False

        i = 1
        while rolled_double == False:

            roll1 = self.die1.roll()
            roll2 = self.die2.roll()

            self.game_log.add_score_entry(ScoreEntry(i, roll1, roll2))
            i += 1

            rolled_double = roll1 == roll2


