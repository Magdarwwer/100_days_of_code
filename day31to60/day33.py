#Day 33 - DYNAMIC LISTS
# add & remove istems as we go

#computer builds a list with nothing in it
myAgenda = []

# def printList():
#   print()
#   for item in myAgenda:
#     print(item)
#   print()

# while True:
#   item = input("What's next on your agenda? >")
#   myAgenda.append(item)
#   stop = input("do you want to add action? >")
#   if stop == "no" or stop == "No":
#     break
#   printList()

# print(myAgenda)

#we could use os i sleep -> we could pause & clean the screen

#2. Removing Items from the list:
# while True:
#   menu = input("add or remove?: ")
#   if menu == "add":
#     item = input("What's next on the Agenda?: ")
#     myAgenda.append(item)
#   elif menu == "remove":
#     item = input("What do you want to remove?: ")
#     if item in myAgenda: # if item in a list
#       myAgenda.remove(item)
#     else:
#       print(f"Item {item} was not found on the list")
#   printList()


#3. Common Errors: added if else removing items that were not on the list

# # #If you see object has no attribute turn around, change their places
# myPartyList = []
# # #4. Fix my code: 
# def printList():
#   print() 
#   for item in myPartyList:
#     print(item)
#   print() 

# while True:
#   menu = input("add or remove?: >")
#   if menu == "add":
#     item = input("Who should I add to the party list?: ")
#     myPartyList.append(item)
#   elif menu == "remove":
#     item = input("Who should I remove from the party list?: ")
#     if item in myPartyList:
#       myPartyList.remove(item)
#     else:
#       print(f"{item} was not in the list")
#   printList()
  
  
#Day 33 - Daily challenge:ToDo List Manager:
toDoList = []

def printList():
  print() 
  for item in toDoList:
    print(item)
  print() 

#First IN First Out - FIFO
print("To Do List Manager:")
#userinput = input("Do you want to view, add, or edit your to do list?")

while True:
  userinput = input("Do you want to view, add, or edit your to do list?")
  if userinput == "add" or userinput == "Add":
    item = input("What do you ADD to the list?: > ")
    #to the bottom of the list.
    toDoList.append(item)
  elif userinput == "edit" or userinput == "Edit":
    item = input("What do you want to edit/remove? > ")
    if item in toDoList:
      toDoList.remove(toDoList[0])
    else:
      print(f"Item {item} was not found on the list")
  elif userinput == "view":
    printList()
  
#could use os & time libraries for cleaning the screen