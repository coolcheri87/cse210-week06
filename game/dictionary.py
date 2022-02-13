# Cheri Hansen  - han19067@byui.edu
# Program is the dictionary for the juumper game
# Created 2/1/2022
# CSE 210-03 W05 Jumper game


import random

class Dictionary:
    
    # This is initializing words and the random word
    def __init__(self):
        self._words = ['core','java','micro','sql','electric','circuits','physics','university','analysis','introduction']
        self._word = self._words[random.randint(0,len(self._words)-1)]
        # For debugging only
        print (self._word)

    def getWord(self):
        return self._word