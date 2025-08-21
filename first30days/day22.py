#Day 22 - libraries!
# # # # Libraries are collections of code that other people have written. 
# Video games often use massive libraries 
# # # (for example: game engines) 
# to create the epic water reflections, 3-D graphics, etc.
# import random

# myRandomNumber = random.randint(1,19920)
# print(myRandomNumber)

#common errors:
import random

# myNumber = random.randint(1, 100)
# print(myNumber)
# print()

# for i in range(10):
#   myNumber = random.randint(1, 100)
#   print(myNumber)
# #------

# for i in range(10):
#   print(random.randint(1, 100))

#DAY 22 - CHALLANGE: using Day 18 -code
print("One-Million-To-One")
attempt_counter = 0
#answer = 256789
answer = random.randint(1,10)
#next time build random number generator

while True:
  attempt_counter += 1
  guess = int(input("What number do you pick? >"))
  if guess < answer and guess > 0:
    print("Too low, go higher")
    continue
  elif guess > answer:
    print("Too high, go lower")
    continue
  elif guess < 0:
    print("I'm done, lol, exit bye!")
    exit()
  elif guess == answer:
    print("You've won! You took ", attempt_counter, " attempts to guess!")
    break
  else:
    print("I dont recognize it as a nnumber, try again")
    continue

print(" Thanks for playing the game!")
print()
