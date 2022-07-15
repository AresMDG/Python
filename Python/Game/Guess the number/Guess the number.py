#2
#* This is a guess the number game, the meaning is that you have 10 attempts to guess the number that the program randomly guessed
import random

guessesTaken = 0
print('Hi, what`s your name?')

myName = input()
number = random.randint(1, 30)
print('Well ' + myName + 'i think of a number 1 to 30')

for guessesTaken in range(10):
   print('Try to guess')
   guess = input()
   guess = int (guess)
   
   if guess < number:
      print('Your number is too small')
   elif guess > number:
      print('You nunmber is too big')
   else:
      break

if guess == number:
   guessesTaken = str(guessesTaken + 1)
   print('Great ' + myName + '! You made it in ' + guessesTaken + ' tries !!!')