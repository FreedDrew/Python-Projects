# How It Works
This README can be used to explain the most important code of the script while using a small amount to demonstrate.



### User is prompted for input R, P, or S
```javascript
print("(R)ock, (P)aper, or (S)cissors?")
	user_choice = input()
```

### The input is related to rock, paper, or scissors using else-if statements
```javascript
	if user_choice == "R" or "r":
		user_choice_value = "rock"
	elif user_choice == "P" or "p":
		user_choice_value = "paper"
```

### The computer selects a random option from a list, then follows same steps as user
```javascript
choices = ['R', 'P', 'S']
computer_choice = (random.choice(choices))
```

### More else-if statements to determine winner (if there is one)
```javascript
if user_choice_value == "rock" and computer_choice_value == "scissors":
		print("Rock beats scissors, you win!!!")
```
