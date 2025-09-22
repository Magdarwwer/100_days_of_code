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
  letter = input("Pick a letter> ").lower()
  if len(letter) == 1:
    if letter not in letterPicked:
      if letter in wordChosen:
        for char in wordChosen:
          if char == letter:
            print(letter, end ='')
          else:
            print("_", end ='')
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