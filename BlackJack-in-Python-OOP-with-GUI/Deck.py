#!/usr/bin/python3

# File name: Deck.py
# Contians the Deck and Card class used in the game of blackjack. 
# Assignment by Victor from the book by Zelle, chapter 10
# Date: 17-12-2016

import sys
from graphics import *
import random

class Deck:
    """A class of a deck of playingcards"""
    def __init__(self):
        self.suit = ["h", "d", "s", "c"]
        self.value = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k"]
        
        # Empty lists for the cards (ordered and shuffled) to go in
        self.deckofcards = [] 
        self.shuffledcards = [] 

        # This loop creates a list with all 52 playingcards
        for suit in self.suit:
            for value in self.value:
                card = suit+value
                self.deckofcards.append(card)

    def Shuffle(self):
        """Shuffles the deck randomly"""
        self.shuffledcards = self.deckofcards
        random.shuffle(self.shuffledcards)
        # Returns new list with shuffled cards
        return self.shuffledcards

    def Deal(self):
        """Returns the first card in the list"""
        card=self.shuffledcards.pop()
        return card

class Card(GraphicsObject):
    """Creates an card-image corresponding to the entered value"""
    def __init__(self, win, value, center):
        self.win = win
        self.centerPoint = center
        self.value = value
        self.card = self.drawCard(value, center) # Generate the Image-object
        self.card.draw(win) # Draw the Image-object

    def getValue(self):
        """Checks the rank of the card and returns the corresponding integer value"""
        picturecards = ["j","q","k"]

        if self.value[1:] in picturecards:
            value = 10
            return int(value)
        else:
            value = self.value[1:]
            return int(value)

    def Undraw(self):
        """Removes the card"""
        self.card.undraw()

    def drawCard(self,value,center):
        """Creates an Image-object of a card with the value as it's name"""
        self.center = center
        self.value = value
        file = "cards_gif/"+str(value)+".gif"
        self.image = Image(center,file)
        return Image(center,file)

