#Day 36 
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

def printList():
  print()
  for i in myList:
    print(i)
  print()

# while True:
#   addItem = input("Item > ")
#   if addItem not in myList:
#     myList.append(addItem) 
#   printList()
  
  ##constantly add something to the list
while True:
  addItem = input("Item > ").strip().capitalize() #changes how it will be stored
  #kolejność of applying functions matter
  #The functions manipulating the strings are applied in the order we add them
  if addItem not in myList:
    myList.append(addItem) 
  printList()