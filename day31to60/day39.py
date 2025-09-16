#Day 39 - Hangman; string slicing, string manipulation:
#This hangman project combines lists, string manipulation, and slicing, along with other concepts.
import random

listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]

wordChosen = random.choice(listOfWords)
print(wordChosen)

letter = input("Pick a letter> ")

#check if just one char len(letter) == 1


#First the word is picked
alphabent = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p","q", "r", "s", "t", "u", "w", "v", "y", "z"]
def remove_letter(letter, list):
  for item in list:
      if item == letter:
        list.remove(letter)
        
life_counter = 5
#Then the user starts to guess letters
while True:
  letter = input("Pick a letter> ")
  if len(letter) == 1:
    if letter in alphabent:
      if letter in wordChosen:
        for char in wordChosen:
          if char == letter:
            print(letter, end ='')
          else:
            print("_", end ='')
      else:
        print("Nope, not in there.")
        print(f"{life_counter} left")
        life_counter =-1
    else:
      print("Letter already used")
      #continue
  else:
    print("Put in a letter man")
    #continue
    
#Track what letters they used


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