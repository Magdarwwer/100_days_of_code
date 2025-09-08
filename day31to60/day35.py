#Day 35 - ToDoList Manager
import os, time
listOfTasks = []

def checkIfexistsandAdd(task):
  if task in listOfTasks:
    print("item already exists in a list")
  else:
    listOfTasks.append(addedTask)
#menu - add, change, remove

def printList():
  print()
  for items in listOfTasks:
    print(items)
  print()

# you can't add duplicates! If input exists - print("it already exists") and move on

while True:
  menu = input("""Do you want to:\n1. view,\n2. add,\n3. edit, or\n 4.remove an item
  from the to do list?\n >""")
  if menu == "add" or menu == "2":
    addedTask = input("What do you want to add to the list? >")
    checkIfexistsandAdd(addedTask)
  elif menu == "edit" or menu == "3":
    whatEdit = int(input("What element do you want to remove? (index)> "))
    #added -1 so the index matches the choice. 
    #can add logic for cheking if user gave number or string and the finding the string in a list or going under the right index
    listOfTasks[(whatEdit-1)] = input("Edit element> ")
  elif menu == "display" or menu == "show" or menu == "view" or menu == "1":
    print(listOfTasks)
  elif menu == "remove" or menu == "4":
    doubleCheck = input("Are you sure you want to remove an element? (yes/no) >")
    if doubleCheck == "yes" or doubleCheck == "YES" or doubleCheck == "Yes":
      whatRemove = int(input("Element at what index you want to remove? >"))
      #listOfTasks.remove(whatRemove)
      del listOfTasks[whatRemove - 1]
    elif doubleCheck == "no" or doubleCheck == "NO" or doubleCheck == "No":
      print("That's what I thought so...")
    else:
      print("no action for that c:")
  else:
    print("ERROR: No action")
  time.sleep(3)
  os.system("clear")
  
  
  #ANOTHER SOLUTION:
#   import os, time
# toDoList = []
# def printList():
#   print()
#   for items in toDoList:
#     print(items)
#   print()
# while True:
#   menu = input("ToDo List Manager\nDo you want to view, add, edit, remove or delete the todo list?\n")
#   if menu=="view":
#     printList()
#   elif menu=="add":
#     item = input("What do you want to add?\n").title()
#     toDoList.append(item)
#   elif menu=="remove":
#     item = input("What do you want to remove?\n").title()
#     check = input("Are you sure you want to remove this?\n")
#     if check[0]=="y":
#       if item in toDoList:
#         toDoList.remove(item)
#   elif menu=="edit":
#     item = input("What do you want to edit?\n").title()
#     new = input("What do you want to change it to?\n").title()
#     for i in range(0,len(toDoList)):
#       if toDoList[i]==item:
#         toDoList[i]=new
#   elif menu=="delete":
#     toDoList = []
#   time.sleep(1)
#   os.system('clear')