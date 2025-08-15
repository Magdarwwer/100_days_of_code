#DAY 23 - Subroutine - call & repeat parts of code. 
from abc import abstractclassmethod


def rollDice():
  import random
  dice = random.randint(1,6)
  print("You rolled ", dice)

for i in range(10):
  rollDice()

#common errors: Just like with variables, you cannot have spaces with subroutines 
# (onlyCamelCase or_using_underscores).
print("----------------")
print()
def MyName():
  print("My Name is David")

MyName()
#2: You need to add () in the first line, even though there is no argument.
print("----------------")
print()
def countToFive():
  for i in range(1, 6):
    print(i)

countToFive()

#3: When you call your subroutine, make sure it is NOT indented.
print("----------------")
print()
def countToFive2():
  for i in range(1, 6):
    print(i)

countToFive2()


#FIX MY CODE TASK:
print()
def printfavoritecolor():
  print("My favorite color is red.")

printfavoritecolor()

#Day 23 CHALLENGE:

print("Replit Login System")
username = "aaa"
password = "bbb"

def login():
  while True:
    print()
    username_input = input("What is your username?: > ") 
    password_input = input("What is your password? > ") 
    if username == username_input and password == password_input:
      print("Welcome to Replit!")
      break
    else:
      print("Whoops! I don't recognize that username or password. Try again!")
      print()
      continue

login()
  
print()
print("Congrats! You remembered your password :3")


