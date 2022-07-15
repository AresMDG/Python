import random

HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''','''
   +---+
       |
        |
        |
       ===''','''
    +---+
    0   |
    |   |
        |
       ===''','''
    +---+
    0   |
   /|   |
        |
       ===''','''
    +---+
    0   |
   /|\  |
        |
       ===''','''
    +---+
    0   |
   /|\  |
   /    |
       ===''','''
    +---+
    0   |
   /|\  |
   / \  |
       ===''',]

words = 'stork shark baboon ram badger beaver bull camel wolf sparrow raven otter dove goose toad zebra snake turkey whale cobra goat goat coyote cow cat rabbit rat chicken llama weasel swan lion fox salmon elk frog bear mollusk moth mule ant mouse mink rhinoceros monkey sheep perch deer eagle donkey panda spider python parrot puma salmon skunk dog owl tiger newt seal duck trout ferret turtle hawk lizard'.split()

def getRandomWord(wordList):
   wordIndex = random.randint(0, len(wordList)-1)
   return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
   print(HANGMAN_PICS[len(missedLetters)])
   print()
   
   print('Wrong letters: ', end = ' ')
   for letter in missedLetters:
      print(letter, end = ' ')
   print()
   
   blanks = '_' * len(secretWord)
   
   for i in range(len(secretWord)):
      if secretWord[i] in correctLetters:
         blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]
         
   for letter in blanks:
      print(letter, end = ' ')
   print()
   
def getGuess(alreadyGuessed):
   while True:
      print('Enter letter: ')
      guess = input()
      guess = guess.lower()
      if len(guess) != 1:
         print('Please enter one letter: ')
      elif guess in alreadyGuessed:
         print('You have already mentioned this letter. name another:')
      elif guess not in 'abcdefghijklmnopqrstuvwxyz':
         print('Please enter a LETTER: ')
      else:
         return guess
      
def playAgain():
   print('Do you want to play more? (Yes or No)')
   return input().lower().startswith('y')

print('G A L L O W S')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDOne = False

while True:
   displayBoard(missedLetters, correctLetters, secretWord)
   guess = getGuess(missedLetters + correctLetters)
      
   if guess in secretWord:
      correctLetters = correctLetters + guess
      foundAllLetters = True
      for i in range(len(secretWord)):
         if secretWord[i] not in correctLetters:
            foundAllLetters = False
            break
         
      if foundAllLetters:
         print('YES! Secret word - "'+ secretWord +'"! You guessed!')
         gameIsDOne = True
   else:
      missedLetters = missedLetters + guess
      
      if len(missedLetters) == len(HANGMAN_PICS) -1:  
         displayBoard(missedLetters, correctLetters, secretWord)
         print('You have exhausted all attempts!\nMissing letters:'+str(len(missedLetters))+'and guessed letters:'+str(len(correctLetters))+'. The word was guessed"'+secretWord+'".' )
         gameIsDOne = True
         
   if gameIsDOne:
      if playAgain():
         missedLetters = ''
         correctLetters = ''
         gameIsDOne = False
         secretWord = getRandomWord(words)
      else:
         break
               