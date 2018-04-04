#write import statement for Die class
from src.homework.homework9.die import Die
'''
Create a Player class.

'''

class Player:

    def __init__(self):
        '''
        Constructor method creates two Die attributes die1 and die2
        '''
        self.die1 = Die()
        self.die2 = Die()


    def roll_doubles(self):
        '''
        The roll_doubles method that will roll die1 and die2 (attributes from constructor method),
        display rolled values,and continue iterating until a double is rolled.
        '''
        not_doubles = True
        while not_doubles:
            roll1 = self.die1.roll()
            roll2 = self.die2.roll()
            print(roll1, roll2)
            if roll1 == roll2:
                not_doubles = False
            
        


