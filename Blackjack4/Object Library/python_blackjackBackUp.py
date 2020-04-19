
import json
from GameFunctions import *
from bjObjects import *

#card_value = ['Ace','2','3','4','5','6','7','8','9','10','J','Q','K']
#card_type = ['Hearts','Spades','Clubs','Diamonds']

# initialize
choice = ""
clear()
players = []
data = {
	"player": "",
	"casino": "",
	"hands": [],  #format of each hand. timestamp, playerHand Arr, dealerHand Arr, win (1/0), #hits, #doubles
}

def game():
	print ("WELCOME TO BLACKJACK!\n")
	deckCount = 2
	deck = Deck(deckCount)
	deck.shuffle()

	#playerName = input("Hello player, what is your name?").lower()
	playerName = "Kody"
	players.append( Player(playerName, 100) )

	#begin recording
	data["player"] = playerName
	data["casino"] = "La Casa de mi Padre"

	#deal first hands
	for player in players:
		player.currentHand = Hand()
		player.currentHand.deal(deck)
	dealerHand = Hand()
	dealerHand.deal(deck)

	#main game loop - runs until request to quit or no players
	#TODO: eventually, remove choice check as exit should occur in for loop
	while len(players) != 0 or choice != "q":
		#shuffles deck if running low
		if len(deck.cards) < 30:
			deck = Deck(deckCount)

		#declare initial hands
		print("You have a \n" + str(player.currentHand) + "\nfor a total of " + str(player.currentHand.total()))
		#check for dealer blackjack. Called this before showing the dealer hand because it's weird to announce their top card then BJ
		#TODO: eventually, end the round at this point if dealer blackjack
		blackjack(dealerHand, player)
		print("The dealer is showing a " + str(dealerHand.hand[0]))

		#handle splits
		#option to hit per hand
		for player in players:
			choice = ""
			#for hand in hands:
			doubleState = True
			while choice != "s" and choice != "d" and player.currentHand.total() < 21:
				if doubleState:
					choice = input("Do you want to [D]ouble down, [H]it, [S]tand, or [Q]uit: ").lower()
					doubleState = False
				else:
					choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
				#clear()
				if choice == "h":
					player.currentHand.hitState = 1
					player.currentHand.hit(deck)
					print("your new card is: " + str(player.currentHand.hand[-1]) + "\nfor a total of " + str(player.currentHand.total()))
				elif choice == "s":
					print( player.name + " stands" )
				elif choice == "d":
					player.currentHand.double = 1
					player.currentHand.hit(deck)
					print("your new card is: " + str(player.currentHand.hand[-1]) + "\nfor a total of " + str(player.currentHand.total()))
				elif choice == "q":
					print("Bye!")
					exit()

		#resolve dealer hand
		while dealerHand.total() < 17:
			dealerHand.hit(deck)

		#check for winner
		score(dealerHand, player)


		#Record & give a chance to leave the game at any time, or after rounds
		for player in players:
			#record test, should record less frequently
			#data["hands"].append((vars(player.currentHand)))

			player.hands.append(player.currentHand)
			choice = input("Do you want to [C]ontinue or [Q]uit: ").lower()
			if choice == "q":
				#TODO: record as player removed
				players.remove( player )
				print("Bye!")
				#print(data)
				exit()

		#deal new hands
		for player in players:
			player.currentHand.newHand()
			player.currentHand.deal(deck)
		dealerHand.newHand()
		dealerHand.deal(deck)
		clear()

def test():
	player = Player("doug",100)
	player.currentHand = Hand()
	player.currentHand.hand = [ Card("D",13), Card("J",14)]

	dealerHand = Hand()
	dealerHand.hand = [ Card("D",11), Card("J",14)]
	hand = [ Card("D",14), Card("J",14)]

	blackjack(dealerHand,player)

if __name__ == "__main__":
	game()
	#test()