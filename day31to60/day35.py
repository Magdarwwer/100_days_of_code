#Day 35 - ToDoList Manager
import os, time
listOfTasks = []

def checkIfexistsandAdd(task):
  if task in listOfTasks:
    print("item already exists in a list")
  else:
    listOfTasks.append(addedTask)
#menu - add, change, remove

while True:
    menu = input("")