#NUMBER GUSSING GAME
import random

number = random.randint(1,100)
# GENERATE A RANDOM NUMBER BETWEEN 1 AND 100
# ASK THE USER GUESS
while True:
   try:
        guess = int(input('guess a number between 1 and 100: '))
        if guess < number:
          print('too low please try again')
        elif guess > number:
          print('too high please try again')
        else:
           print('WOW CONGRATS YOU GUESSED IT CORRECT WELL DONE') 
           break   
   except ValueError:
          print('please enter a valid number')

# MAKE SURE USER ENTER A VALID NUMBER
# IF INVALID NUMBER PRINT INVALID
# ELSE IF ITS VALID COMPARE THE GUESS AND 
# PRINT IF ITS LOWER LOWER NUMBER ELSE PRINT HIGHER NUMBER
# ELSE THE NUMBER MUST BE SAME SO PRINT ITS  CORRECT
# #