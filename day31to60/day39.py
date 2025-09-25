#Day 39 - Hangman; string slicing, string manipulation:
#This hangman project combines lists, string manipulation, and slicing, along with other concepts.
import random, os, time

listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]

wordChosen = random.choice(listOfWords)
print(wordChosen)

letter = input("Pick a letter> ")

#check if just one char len(letter) == 1

letterPicked = []
#First the word is picked
# alphabent = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p","q", "r", "s", "t", "u", "w", "v", "y", "z"]
def remove_letter(letter, list):
  for item in list:
      if item == letter:
        list.remove(letter)
        
life_counter = 6
#Then the user starts to guess letters
while True:
  time.sleep(1)
  os.system("clear")
  allLetters = True
  letter = input("Pick a letter> ").lower()
  if len(letter) == 1:
    if letter not in letterPicked:
      if letter in wordChosen:
        for char in wordChosen:
          if char == letter:
            print("You found a letter")
            print(letter, end ='')
            letterPicked.append(letter)
            allLetters = False
          else:
            print("_", end ='')
            allLetters = False
      else:
        print("Nope, not in there.")
        life_counter -=1
        print(f"{life_counter} left")
        
    else:
      print("Letter already used")
      #continue
  else:
    print("Put in a letter man")
    #continue
    
        
if life_counter > 0:# and # 
    print("you win")
print()
#Track what letters they used

#Keep track of letters used. Try adding each letter chosen to a new list, then checking this list for each subsequent choice.

#ASCII HANGMAN:
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# import random, os, time

# listOfWords = ["apple", "orange", "grapes", "pear"]
# letterPicked = []
# lives = 6

# word = random.choice(listOfWords)

# while True:
#   time.sleep(1)
#   os.system("clear")
#   letter = input("Choose a letter: ").lower()
  
#   if letter in letterPicked:
#     print("You've tried that before")
#     continue
    
#   letterPicked.append(letter)
  
#   if letter in word:
#     print("You found a letter")
#   else:
#     print("Nope, not in there")
#     lives -= 1
  
#   allLetters = True
#   print()
#   for i in word:
#     if i in letterPicked:
#       print(i, end="")
#     else:
#       print("_", end="")
#       allLetters = False
#   print()

#   if allLetters:
#     print(f"You won with {lives} left!")
#     break

#   if lives<=0:
#     print(f"You ran out of lives! The answer was {word}")
#     break
#   else:
#     print(f"Only {lives} left")