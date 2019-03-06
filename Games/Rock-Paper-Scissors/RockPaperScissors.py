import random
import sys

print("========================================================")
print("			    Rock Paper Scissors						   ")
print("========================================================")
print("Winning Rules of the Rock paper scissor game as follows:")
print("*	Rock beats scissors")
print("*	Scissors beats paper")
print("*	Paper beats rock")
print("========================================================")
print("Whats your name? ")
user_name = input()
print("========================================================")
print("Hey " + user_name + ", thanks for playing my game!")
print("--------------------------------------------------------")
print("Lets get started!!!")
print()

repeat = True
while repeat == True:
	print("(R)ock, (P)aper, or (S)cissors?")
	user_choice = input()
	print("--------------------------------------------------------")
	if user_choice == "R" or "r":
		user_choice_value = "rock"
	elif user_choice == "P" or "p":
		user_choice_value = "paper"
	elif user_choice == "S" or "s":
		user_choice_value = "scissors"
	else:
		print("OOPS!!! That's not an option.")
	print("You chose " + user_choice_value)
	print("--------------------------------------------------------")

	choices = ['R', 'P', 'S']
	computer_choice = (random.choice(choices))
	if computer_choice == "R":
		computer_choice_value = "rock"
	elif computer_choice == "P":
		computer_choice_value = "paper"
	elif computer_choice == "S":
		computer_choice_value = "scissors"
	print("The computer chose " + computer_choice_value)
	print("--------------------------------------------------------")

	if user_choice_value == "rock" and computer_choice_value == "scissors":
		print("Rock beats scissors, you win!!!")
		print("========================================================")
	elif user_choice_value == "scissors" and computer_choice_value == "paper":
		print("Scissors beat paper, you win!!!")
		print("========================================================")
	elif user_choice_value == "paper" and computer_choice_value == "rock":
		print("Paper beats rock, you win!!!")
		print("========================================================")
	elif user_choice_value == "paper" and computer_choice_value == "scissors":
		print("Scissors beat paper, you lose!!! :(")
		print("========================================================")
	elif user_choice_value == "scissors" and computer_choice_value == "rock":
		print("Rock beats scissors, you lose!!! :(")
		print("========================================================")
	elif user_choice_value == "rock" and computer_choice_value == "paper":
		print("Paper beats rock, you lose!!! :(")
		print("========================================================")
	else:
		print("You both chose the same option, it's a tie!!!")
		print("========================================================")


	print("Play again? (Y/N)")
	play_again = input()
	print("========================================================")
	if play_again == "Y" or "y":
		repeat
	else:
		print("Come back soon " + user_name + "!")
		sys.exit()




