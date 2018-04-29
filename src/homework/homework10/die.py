#Write an import statement for the Python random module
import random

'''
Create a Die class to model a game day with 6 sides and values 1,2,3,4,5, and 6.
Define a constructor method with one attribute sides with a values of 6.
Defina a roll method that virtually rolls a die and returns the value. 
'''

class Die:

    def __init__(self):
        self.sides = 6
        self.value = 6

    def roll(self):
        self.value = random.randint(1, self.sides)
        return self.value


