import os
import random

def play_again():
	again = input("Do you want to play again? (Y/N) : ").lower()
	if again == "y":
		dealer_hand = []
		player.currentHand = []
		deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
		game()
	else:
		print ("Bye!")
		exit()

def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')

#if happy with print, delete comments
def print_results(dealer_hand, player_hand): #name, hand):
	clear()
	print ("The dealer has a \n" + str(dealer_hand) + "\nfor a total of: " + str(dealer_hand.total())+ "\n")
	print ("You have a \n" + str(player_hand) + "\nfor a total of: " + str(player_hand.total())+ "\n")
	#print(name + "has a \n" + str(hand) + "\nfor a total of: " + str(hand.total() ))

#Note: assumes called before players hit, doesnt account for hand bigger than 2 cards
def blackjack(dealer_hand, player):
	if player.currentHand.total() == dealer_hand.total() == 21:
		print("you both received blackjack, push")
	elif player.currentHand.total() == 21:
#		print_results(player.currentHand)
		print ("Congratulations! You got a Blackjack!\n" + str(player.currentHand))
		player.currentHand.blackjack = 1
		player.currentHand.win = 1
	elif dealer_hand.total() == 21:
#		print_results(dealer_hand, player.currentHand)
		print ("Sorry, you lose. The dealer got a blackjack.\n"+ str(dealer_hand))
		dealer_hand.blackjack = True

def score(dealer_hand, player):
	print_results(dealer_hand, player.currentHand)
	if player.currentHand.total() == 21 and len(player.currentHand.hand) == 2:
		print ("Congratulations! You got a Blackjack!\n")
	elif dealer_hand.total() == 21 and len(dealer_hand.hand) == 2:
		print ("Sorry, you lose. The dealer got a blackjack.\n")
	elif player.currentHand.total() > 21:
		print ("Sorry. You busted. You lose.\n")
	elif dealer_hand.total() > 21:
		print ("Dealer busts. You win!\n")
	elif player.currentHand.total() < dealer_hand.total():
		print ("Sorry. Your score isn't higher than the dealer. You lose.\n")
	elif player.currentHand.total() > dealer_hand.total():
		print ("Congratulations. Your score is higher than the dealer. You win\n")
	elif player.currentHand.total() == dealer_hand.total():
		print ("Hand is a push, players tied")
	else:
		print ("something has gone wrong with score() if this appears")
