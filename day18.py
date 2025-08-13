#Day 18 - guess the number| WHILE LOOP
print("One-Million-To-One")
attempt_counter = 0
answer = 256789
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
  else:
    print("You've won! You took ", attempt_counter, " attempts to guess!")
    break

print(" Thanks for playing the game!")
print()
