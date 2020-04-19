import os
import random

def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')

#if happy with print, delete comments
def print_results(dealerHand, player_hand): #name, hand):
	clear()
	print ("The dealer has a \n" + str(dealerHand) + "\nfor a total of: " + str(dealerHand.total())+ "\n")
	print ("You have a \n" + str(player_hand) + "\nfor a total of: " + str(player_hand.total())+ "\n")
	#print(name + "has a \n" + str(hand) + "\nfor a total of: " + str(hand.total() ))

#Note: assumes called before players hit, doesnt account for hand bigger than 2 cards
#todo: should this be adjusted to a hand instead of player?
#todo: pretty sure this won't work for splits
def blackjack(dealerHand, player):
	if player.currentHand[0].total() == dealerHand.total() == 21:
		print("you both received blackjack, push")
		playerHand.win = 2
	elif player.currentHand[0].total() == 21:
#		print_results(player.currentHand)
		print ("Congratulations! You got a Blackjack!\n" + str(player.currentHand[0]))
		player.currentHand[0].blackjack = 1
		player.currentHand[0].win = 1
	elif dealerHand.total() == 21:
#		print_results(dealerHand, player.currentHand)
		print ("Sorry, you lose. The dealer got a blackjack.\n"+ str(dealerHand))
		dealerHand.blackjack = 1

def score(dealerHand, playerHand):
	#todo if code breaks, re-add blackjack check. Otherwise, assume blackjacks are handled earlier in logic
	print("Dealer Hand:" + str(dealerHand) + " for a score of: " + str(dealerHand.total()))
	print("Player Hand:" + str(playerHand) + " for a score of: " + str(playerHand.total()))

	#ties dealerHand to player for results later
	playerHand.dealerHand = dealerHand.hand
	playerHand.dealerScore = dealerHand.total()
	playerHand.score = playerHand.total()

	if playerHand.total() > 21:
		print ("Sorry. You busted. You lose.\n")
	elif dealerHand.total() > 21:
		print ("Dealer busts. You win!\n")
		playerHand.win = 1
	elif playerHand.total() < dealerHand.total():
		print ("Sorry. Your score isn't higher than the dealer. You lose.\n")
	elif playerHand.total() > dealerHand.total():
		print ("Congratulations. Your score is higher than the dealer. You win\n")
		playerHand.win = 1
	elif playerHand.total() == dealerHand.total():
		print ("Hand is a push, players tied")
		playerHand.win = 2
	else:
		print ("something has gone wrong with score() if this appears")
