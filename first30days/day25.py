# DAY 25
# This is where we see a concept called scope. Scope is a variable only available from inside the region it was created.
# Variables that are created for the first time in a subroutine are only available inside that subroutine.
# We cannot call the variable area outside the subroutine.
# We need to create the variable area inside the subroutine.
#Day 25 - deeper into subroutines - RETURN
#return sends some information back to the part of code
#that called it
import random
#This means the function call is replaced with whatever was returned.

#1
def myName():
  return "david"

print(myName())

print()
#2
#subroutine has parameter called `number`
#`number` shows how many numbers we want the pin to have
def pinPicker(number):
  #import random
  pin = "" #this is the empty string
  for i in range(number): #for loop shows defined amount of random numbers
    pin += str(random.randint(0,9)) #we want a string of random numbers between 0-9
  return pin
    
print(pinPicker(4)) #4 means we want 4 random numbers

myPin = pinPicker(4)
print(myPin)
print()
#3 Common Errors:
def areaOfTriangle(base, height):
  area = 0.5 * base * height
  return area

area = (areaOfTriangle (5, 22))
print(area)

print()
#4 Name error - area not visible:
#Scope is a variable only available from inside the region it was created.
#Variables that are created for the first time in a subroutine are only 
#available inside that subroutine.
def areaOfTriangle2(base, height):
  area = 0.5 * base * height
  return area

area1= areaOfTriangle2(5, 22)
print(area1)

print()
#5 Fix my code:
def area_square(side1, side2):
  area_square = side1 * side2
  return area_square

area = area_square(4, 12)
print(area)

#6 DAY 25 CHALLENGE - CHaracter STat Generator:

print("Character Stats Generator ")
sides = int(input("Give me a number of sides >"))

def rollDiceretNumber(sides):
    rolled_side = random.randint(1,sides)
    return rolled_side

def healthDice():
  six_dice_number = rollDiceretNumber(6)
  eight_dice_number = rollDiceretNumber(8)
  health = six_dice_number * eight_dice_number
  return health

play_again = "yes"

# print("Roll the infinite dice:")
# print(rollDiceretNumber(sides))
# print()

while play_again == "yes" or play_again == "Yes":
  char_name = input("Name your warrior: >")
  char_health = str(healthDice())
  print("Their health is: ", char_health)
  print()
  play_again= input("Want to play again? >")

print("We done, thx")