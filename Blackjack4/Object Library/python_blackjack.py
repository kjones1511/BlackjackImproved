
import time
from GameFunctions import *
from DatabaseFunctions import *

#card_value = ['Ace','2','3','4','5','6','7','8','9','10','J','Q','K']
#card_type = ['Hearts','Spades','Clubs','Diamonds']

# initialize
choice = ""
clear()
players = []
data = {
	"player": "",
	"casino": "",
	"hands": []  #format of each hand. timestamp, playerHand Arr, dealerHand Arr, win (1/0), #hits, #doubles
}

#temp
casino = "La Casa De Mi Padre"
deckCount = 2
def game():
	#get mongoDB collection pointer
	coll = LaunchConnection()

	#todo: figure out how to handle Dealer in dealFirstHand()
	dealerHand = Hand()

	print ("WELCOME TO BLACKJACK!\n")
	# deckCount = 2
	# deck = Deck(deckCount)
	# deck.shuffle()
	#
	# #playerName = input("Hello player, what is your name?").lower()
	# playerName = choice = input("Enter Player Name:  ")
	# players.append( Player(playerName, 100) )
	#
	# #begin recording
	# data["player"] = playerName
	# data["casino"] = "La Casa de mi Padre"
	#
	# #deal first hands

	###INITIALIZE phase
	#creates a deck, with deckCount decided by casino
	deck = initializeDeck(deckCount)
	initializeOnePlayer(players, data, casino)

	#todo: repair dealFirstHand once resolved confilct with referencing player in initial Blackjack check.
	# Probably requires making blackjack just check 1 player at a time
	#dealFirstHand(players, dealerHand, deck)
	for player in players:
		player.currentHand.append( Hand() )
		player.currentHand[0].deal(deck)
	dealerHand = Hand()
	dealerHand.deal(deck)

	#TODO add code to record decks

	#TODO delete this test CODE
	# deck.cards[-1] = Card("D",7)
	# deck.cards[-2] = Card("J", 8)
	# players[0].currentHand[0].hand = [ Card("H",7), Card("H",7)]

	#main game loop - runs until request to quit or no players
	while len(players) != 0 or choice != "q":
		#shuffles deck if running low
		if len(deck.cards) < 30:
			deck = Deck(deckCount)

		#check for dealer blackjack. Called this before showing the dealer hand because it's weird to announce their top card then BJ
		#TODO: eventually, end the round at this point if dealer blackjack
		blackjack(dealerHand, player)
		blackjack(dealerHand, player)
		print("The dealer is showing a " + str(dealerHand.hand[0]))

		#handle splits
		#option to hit per hand
		for player in players:
			#TODO HANDLE BLACKJACK FOR SPLITS
			i = 0
			while i < len(player.currentHand):
				if player.currentHand[i].splitCheck():
					clear()
					choice = input("[Y/N] Would you like to Split this hand?: \n" + str(player.currentHand[i]) + "\n").lower()
					if choice == "y":
						player.split( i,deck)
						print("New hands for " + player.name + ":")
						print( player.currentHand[i])
						print(player.currentHand[i+1])
						time.sleep(1)
					else:
						i += 1
				else:
					i += 1

			for thisHand in player.currentHand:
				clear()
				choice = ""
				#for hand in hands:
				doubleState = True
				while choice not in ["s","d","q"] and thisHand.total() < 21:
					print("Player:" + player.name + "\nHand:" + str(thisHand) + "\nScore:" + str(thisHand.total()) )
					if doubleState:
						choice = input("Do you want to [D]ouble down, [H]it, or [S]tand: ").lower()
						doubleState = False
					else:
						choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
					#clear()
					if choice == "h":
						thisHand.hitState = 1
						thisHand.hit(deck)
						print("your new card is: " + str(thisHand.hand[-1]) + "\nfor a total of " + str(thisHand.total()))
					elif choice == "s":
						print( player.name + " stands" )
					elif choice == "d":
						thisHand.double = 1
						thisHand.hit(deck)
						print("your new card is: " + str(thisHand.hand[-1]) + "\nfor a total of " + str(thisHand.total()))
					time.sleep(1)
					clear()

		#resolve dealer hand
		while dealerHand.total() < 17:
			dealerHand.hit(deck)

		#Score, Record & give a chance to leave the game at any time, or after rounds
		#NOTE: Scoring shouldn't occur if there are 0 players in game
		for player in players:
			for thisHand in player.currentHand:
				clear()
				#check for winner
				score(dealerHand, thisHand)

				#compress hand to JSON, append to dictionary
				x = json.dumps(thisHand.__dict__, default=lambda o: o.__dict__)
				data["hands"].append(  json.loads(x)  )

				#TODO: unless i decide to compress the whole player, this line is unecessary
				player.hands.append(thisHand)

				time.sleep(2.5)

			choice = input("Do you want to [C]ontinue or [Q]uit: ").lower()
			if choice == "q":
				#pushes data JSON to collection, todo make this work for mult players by requesting data per player
				coll.insert_one( data )
				players.remove( player )
				print("Goodbye" + player.name + "!")
				#print(data)

		#deal new hands
		for player in players:
			player.currentHand = [Hand()]
			player.currentHand[0].newHand(deck)
		dealerHand.newHand(deck)
		clear()
	exit()

def test():
	client = MongoClient(
		"mongodb+srv://root:chicago1%21@blackjackanalytics-idjco.mongodb.net/Results?retryWrites=true&w=majority&authSource=admin")
	db = client.Results
	coll = db.TestColResults

	player = Player("kile", 100)
	card1 = Card("S", 7)
	card2 = Card("D", 7)
	card3 = Card("D", 7)
	deck = Deck(2)
	deck.shuffle()
	hand = Hand()
	player.currentHand.append(hand)
	player.currentHand[0].hand = [card1, card2, card3]

	data = {
		"player": "take2",
		"casino": "",
		"hands": []  # format of each hand. timestamp, playerHand Arr, dealerHand Arr, win (1/0), #hits, #doubles
	}

	for hand in player.currentHand:
		data = json.dumps(player.__dict__, default=lambda o: o.__dict__)
		coll.insert_one(data)


# print( vars(card1) )
# print(vars(player.currentHand[0]))


if __name__ == "__main__":
	game()
	#test()