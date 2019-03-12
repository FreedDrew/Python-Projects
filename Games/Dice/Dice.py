from sys import exit
import random
import time

low = 1
high = 6

player_roll = 0
computer_roll = 0

print(""" 
        :::::::::::::::::::::::::::
        ::        Welcome        ::  
        ::          to           ::
        ::       Dice Roll!      :: 
        :::::::::::::::::::::::::::            """)
print("===========================================")
player_name = input("Enter your name please: ")
print("===========================================")
print()
print("Hello " + player_name + "!!!")
print()
print("=================================================================================================")
print("The rules are simple, you and the computer will roll dice and whoever rolls a higher number wins!")
print("=================================================================================================")
time.sleep(5)

roll_again = "yes"
while roll_again == "yes":
    if roll_again == "no":
        exit(0)
    print()
    print(player_name + "'s Turn")
    print()
    time.sleep(1)
    print("Rolling...")
    time.sleep(2)

    player_roll = random.randint(low, high)
    computer_roll = random.randint(low, high)


    def dice(die):
        if die == 1:
            print(""" 
        :::::::::::::::::
        ::             ::  
        ::      O      ::
        ::             :: 
        ::::::::::::::::: """)

        elif die == 2:
            print(""" 
        :::::::::::::::::
        ::         O   ::  
        ::             ::
        ::   O         :: 
        ::::::::::::::::: """)

        elif die == 3:
            print(""" 
        :::::::::::::::::
        ::         O   ::  
        ::      O      ::
        ::   O         :: 
        ::::::::::::::::: """)

        elif die == 4:
            print(""" 
        :::::::::::::::::
        ::   O     O   ::  
        ::             ::
        ::   O     O   :: 
        ::::::::::::::::: """)

        elif die == 5:
            print(""" 
		:::::::::::::::::
		::   O     O   ::  
		::      O      ::
		::   O     O   :: 
		::::::::::::::::: """)

        elif die == 6:
            print("""   
	   :::::::::::::::::
	   ::   O     O   ::  
	   ::   O     O   :: 
	   ::   O     O   :: 
	   :::::::::::::::::  """)


    dice(player_roll)

    print()
    time.sleep(1)
    print()
    print()
    print()
    print("Computer's Turn")
    time.sleep(1)
    print()
    print("Rolling...")
    time.sleep(2)

    dice(computer_roll)

    time.sleep(1)

    if player_roll == computer_roll:
        print()
        print()
        print()
        print("IT'S A TIE!!!")
        time.sleep(1)
        print()
        print("=======================================================")
        print("Type yes if you want to play again, or no if you don't!")
        print("=======================================================")
        print()

    elif player_roll > computer_roll:
        print()
        print()
        print()
        print("YOU WIN!!!")
        time.sleep(1)
        print()
        print()
        print()
        print("=======================================================")
        print("Type yes if you want to play again, or no if you don't!")
        print("=======================================================")
        print()
    elif player_roll < computer_roll:
        print()
        print()
        print()
        print("YOU LOST!!! :(")
        time.sleep(1)
        print("=======================================================")
        print("Type yes if you want to play again, or no if you don't!")
        print("=======================================================")
        print()

    roll_again = input("Play again?")
print()
print()
