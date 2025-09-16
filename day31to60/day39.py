#Day 39 - Hangman; string slicing, string manipulation:
#This hangman project combines lists, string manipulation, and slicing, along with other concepts.
import random

listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]

wordChosen = random.choice(listOfWords)
print(wordChosen)

letter = input("Pick a letter> ")

#check if just one char len(letter) == 1
