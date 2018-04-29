#Write an import statement for the Python random module
import random

'''
Base Die class to model a die
Define a constructor method with class attribute sides and value.
Defina a roll method that virtually rolls a die and returns the value. 
'''

class Die:

    #HOMEWORK12: modify the constructor parameter list to include sides
    def __init__(self, sides):
        self.sides = sides
        self.value = 0

    def roll(self):
        self.value = random.randint(1, self.sides)
        return self.value


