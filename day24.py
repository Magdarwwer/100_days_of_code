#Day 24 - parameters:

def whichCake(ingredient):
  if ingredient == "chocolate":
    print("Mmm, chocolate cake is amazing")
  elif ingredient == "broccoli":
    print("You what mate?!")
  else: 
    print("Yeah, that's great I suppose...")

whichCake("chocolate")
print()
whichCake("strawberries")

#2: Adding more arguments:
def whichCake2(ingredient, base, coating):
  if ingredient == "chocolate":
    print("Mmm, chocolate cake is amazing")
  elif ingredient == "broccoli":
    print("You what mate?!")
  else: 
    print("Yeah, that's great I suppose...")
  print("So you want a", ingredient, "cake on a", base, "base with", coating, "on top?")

whichCake2("carrot", "biscuit", "icing")

#3: user inputs the ingredient
def whichCake3(ingredient, base, coating):
  if ingredient == "chocolate":
    print("Mmm, chocolate cake is amazing")
  elif ingredient == "broccoli":
    print("You what mate?!")
  else: 
    print("Yeah, that's great I suppose...")
  print("So you want a", ingredient, "cake on a", base, "base with", coating, "on top?")

userIngredient = input("Name an ingredient: ")
userBase = input("Name a type of base: ")
userCoating = input("Fave cake topping: ")
whichCake3(userIngredient, userBase, userCoating)

#4: common errors:
def biggerNumber(number1, number2):
  if(number1 > number2):
    print(number1, "is bigger")
  else:
    print(number2, "is bigger")

biggerNumber (18,332)

#5: fix my code:
print()
print("----------------")
print("PIZZA ORDER:")
def pizza_order(topping1, topping2):
  if topping1 == "pepperoni":
    print(topping1, "is a great choice")
  else:
    print(topping1, "is kinda lame on pizza")
  print(topping2, "sounds delicious, much better than", topping1)
  
topping1 =  input("Name a pizza topping. ")
topping2 = input("Name a second pizza topping. ")

pizza_order(topping1, topping2)

#6 DAY 24 Challenge - write a subroutine for rolling a dice with as many sides as i want
# why don't i have to set data type in argument? lol 

import random

sides = int(input("How many sides?: >"))
roll_again = "yes"

def infinityDice(sides):
    print("You rolled: ", random.randint(1,sides))
  
while roll_again == "yes" or roll_again == "Yes":
      infinityDice(sides)
      roll_again = input("Roll again? >")

#insted of having while in a function - we call the function again and again in 
#a while outside the function

#aha, im not giving new number of sides every time. I just give it once lol. it then 
#generates random numbers automatically