#Day 35 - ToDoList Manager
import os, time
listOfTasks = []

def checkIfexistsandAdd(task):
  if task in listOfTasks:
    print("item already exists in a list")
  else:
    listOfTasks.append(addedTask)
#menu - add, change, remove

# you can't add duplicates! If input exists - print("it already exists") and move on

while True:
  menu = input("""Do you want to:\n1. view,\n2. add,\n3. edit, or\n 4.remove an item
  from the to do list?\n >""")
  if menu == "add" or menu == "2":
    addedTask = input("What do you want to add to the list? >")
    checkIfexistsandAdd(addedTask)
  elif menu == "edit" or menu == "3":
    whatEdit = int(input("What element do you want to remove? (index)> "))
    listOfTasks[whatEdit] = input("Edit element> ")
  elif menu == "display" or menu == "show" or menu == "view" or menu == "1":
    print(listOfTasks)
  elif menu == "remove" or menu == "4":
    doubleCheck = input("Are you sure you want to remove an element? (yes/no) >")
    if doubleCheck == "yes" or doubleCheck == "YES" or doubleCheck == "Yes":
      whatRemove = int(input("Element at what index you want to remove? >"))
      listOfTasks.remove(whatRemove)
    elif doubleCheck == "no" or doubleCheck == "NO" or doubleCheck == "No":
      print("That's what I thought so...")
    else:
      print("no action for that c:")
  else:
    print("ERROR: No action")
  time.sleep(3)
  os.system("clear")