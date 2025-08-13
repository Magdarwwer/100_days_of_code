#Day 16 - infinite loops, boolean, break vs continue
#infinite loop:
# while True:
#   print("This program is running")
# print("Aww, I was having a good time 😭")
#1----Forcible INFINITE loop with break statement to stop
# while True:
#   print("This program is running")
#   goAgain = input("Go again?: ")
#   if goAgain == "no":
#     break
# print("Aww, I was having a good time 😭")
#2------------------
# counter = 0
# while True:
#   answer = int(input("Enter a number: "))
#   print("Adding it up!")
#   counter += answer
#   print("Current total is", counter)
#   addAnother = input("Add another? ")
#   if addAnother == "no":
#     break
# print("Bye!")
#3----------error fix:
# while True:
#   color = input("Enter a color: ")
#   if color == "red":
#     break
#   else:
#     print("Cool color!")
# print("I don't like red")
#4-----Daily Challenge:
print("Fill in the blank lyrics!")
counter = 1
print("Type in the blank lyrics and see if you are as cool as me.")
print()
guess = "bbb"
answer = "give"

while guess!= answer:
  guess = input("Never going to ______ you up. >")
  if guess != answer: 
    print("Nope, try again.")
  else:
    print("Well done! It only took you", counter,"attempts")
  counter+=1
  print()
#5------------------
# print("Welcome to Name the Song Lyric")
# print()
# print("Figure out the missing word as quickly as you can!")
# print()

# counter = 1

# while True:
#   lyrics = input("I don't wanna ______ a thing. >")
#   if lyrics == "miss" or lyrics == "Miss":
#     print("You got it")
#     break
#   else:
#     print("Nope, try again!")
#     counter += 1
# print("Thanks for playing!")

# print("You got the correct lyrics in", counter, "attempt(s).")
