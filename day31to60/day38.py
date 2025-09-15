#Day 38 - combine Strings & Loops 
#strings are lists in disguise
vowels = ["a", "e", "i", "o", "u"]
#a lot of
myString = "Day 38"
myString = input("Type something> ")
for letter in myString:
  if letter.lower() in vowels:#== "a":
    print('\033[33m', end='')
print(letter, end = '')
print('\33[0m', end = '')

# This code outputs:
#D
#a
#y

#3
#8
# this is a comment in the code, the computer will ignore it
