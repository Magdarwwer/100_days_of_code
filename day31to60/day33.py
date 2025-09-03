#Day 33 - DYNAMIC LISTS
# add & remove istems as we go

#computer builds a list with nothing in it
myAgenda = []

def printList():
  print()
  for item in myAgenda:
    print(item)
  print()

while True:
  item = input("What's next on your agenda? >")
  myAgenda.append(item)
  stop = input("do you want to add action? >")
  if stop == "no" or stop == "No":
    break
  printList()

print(myAgenda)