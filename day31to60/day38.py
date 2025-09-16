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

#Daily challenge 38:
user_input = input("\n'\033[33m'Write a sentence > '\33[0m'")

print("FOR:")
for letter in user_input:
  if letter.lower() == "r":
    print('\033[31m', end="")
  elif letter.lower() == "b":
    print('\033[34m', end="")
  elif letter.lower() == "g":
    print('\033[92m', end="")
  elif letter.lower() == "y":
    print('\033[93m', end="")
  elif letter.lower() == "p":
    print('\033[35m', end="")
  elif letter.lower() == "o":
    print('\033[33m', end="")
  elif letter == " ":
    print('\33[0m', end = '')
  elif letter.lower() == "m":
    print('\33[95m', end = '')
  else:
    print('\33[0m', end = '')
  print(letter, end ='')


#second approach:
def colorChange(letter):
  if letter.lower() == "r":
    print('\033[31m', end="")
  elif letter.lower() == "b":
    print('\033[34m', end="")
  elif letter.lower() == "g":
    print('\033[92m', end="")
  elif letter.lower() == "y":
    print('\033[93m', end="")
  elif letter.lower() == "p":
    print('\033[35m', end="")
  elif letter.lower() == "o":
    print('\033[33m', end="")
  elif letter == " ":
    print('\33[0m', end = '')
  elif letter.lower() == "m":
    print('\33[95m', end = '')
  else:
    print('\33[0m', end = '')

for letter in user_input:
  colorChange(letter.lower())
  print(letter, end ='')
print()