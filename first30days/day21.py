#Day 21 - MATH GAME - multiplication
print("Math Game!")
print()

points = 0
x = int(input("Name your multiples: >"))


for i in range(1,11):
  print(i, " x ", x, "=")
  answer = int(input(">"))

  if answer == i*x:
    print("Good job!")
    points +=1
  else:
    print("No points for you this time... The answer is ", i*x)

print()
print("You scored ",points," out of 10")
