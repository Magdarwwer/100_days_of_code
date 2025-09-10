#Day 36 
import os, time
name = input("What's your name? : ")
if name.lower().strip() == "david" or name.lower() == "magda":
  print(f"Hello {name}")
else:
  print("I don't know you")
  
ourTitle = "this is our title "
print(f"using .title() :{ourTitle.title()}")
print(f"using .upper() :{ourTitle.upper()}")
print(f"using capitalize(): {ourTitle.capitalize()}")

#.strip() - removes spaces
#NO DUPLICATES:
myList = []

def printList(argumentlist):
  print()
  for i in argumentlist:
    print(i)
  print()

# while True:
#   addItem = input("Item > ")
#   if addItem not in myList:
#     myList.append(addItem) 
#   printList()
  
  ##constantly add something to the list
# while True:
#   addItem = input("Item > ").strip().capitalize() #changes how it will be stored
#   #kolejność of applying functions matter
#   #The functions manipulating the strings are applied in the order we add them
#   if addItem not in myList:
#     myList.append(addItem) 
#   printList()
  
#   #Fix my code:
# whatToEat = input("What do you fancy for dinner? ")

# if whatToEat.strip().lower() == "pasta": 
#   print("Get out the pasta maker.")
# elif whatToEat.strip().upper() == "TACOS":
#   print("Let's do Taco Tuesday!")
# else: 
#   print("Go search the fridge.")
  
#Day 36 challenge - create a list with people names
# ask for name, surname
#every time you add a name you display it

namesList = []
stopvar = "yes"
while True:
  if stopvar.strip().lower() == "yes":
    name = input("Plesae provide a name >").strip().capitalize()
    surname = input("Please provide a surname >").strip().capitalize()  
    if name not in namesList and surname not in namesList:
      namesList.append(name)
      namesList.append(surname)
    
    printList(namesList)
    
    stopvar = input("Do you want to continue? yes/no >")
    time.sleep(3)
    os.system("clear")
  elif stopvar.strip().lower() == "no":
    break
  else:
    print("wrong input, bye")
    time.sleep(2)
    os.system("clear")
    break

print("bye")