#3
import random
import time

def displayIntro():
   print('''You are in the lands inhabited by dragons.
In front of you you see two caves. In one of them is a friendly dragon,
who is ready to share his treasures with you. In the second -
Greedy and hungry dragon that will eat you in a flash.''')
   
def chooseCave():
   cave = ''
   while cave != '1' and cave != '2':
      print('Which cave will you enter? (press key 1 or 2)')
      
      cave = input()
   
   return cave

def checkCave(chooseCave):
   print('You are approaching a cave...')
   time.sleep(3)
   print('Its darkness makes you tremble with fear...')
   time.sleep(3)
   print('A big dragon jumps out in front of you! He opens his mouth and...')
   time.sleep(3)
   
   friendlyCave = random.randint(1, 2)
   
   if chooseCave == str(friendlyCave):
      print('...sharing his treasures with you!')
   else:
      print('... instantly eats you up!')
      
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
   displayIntro()
   caveNumber = chooseCave()
   checkCave(caveNumber)
   
   print('Try again? (yes or no)')
   playAgain = input()