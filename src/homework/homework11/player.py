from src.homework.homework11.score_entry import ScoreEntry
from src.homework.homework11.die import Die

class Player:

    #ASSIGNMENT 12: modify the constructor parameter list and add die1 and die2 as parameters.
    def __init__(self, game_log, die1, die2):
        self.die1 = die1 #ASSIGNMENT12: update the statement to use the die1 parameter argument
        self.die2 = die2 #ASSIGNMENT12: update the statement to use the die2 parameter argument
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


