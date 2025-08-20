# #1) a += dla listy i stringa oznacza „rozbij string na literki i dodaj każdą literkę osobno do listy”
# WHY ERROR?
# heroes_names to lista.
# character_name to string.
# += w tym przypadku oznacza „dodaj każdy znak stringa osobno do listy” → działa, ale nie tak jak chcesz.
# heroes_health to lista.
# character_health to float.
# tutaj += nie działa, bo float nie jest iterowalny → stąd błąd: not supported for types list and float.

# heroes_names = []
# heroes_names += "Aria"
# print(heroes_names)  
# # wynik: ['A', 'r', 'i', 'a']

#2) To add a whole object to the list 👉 Rozwiązanie: zamiast += użyj .append():

# heroes_names.append(character_name)
# heroes_health.append(character_health)
# heroes_attack.append(character_strength)


#3) Saving hero as a DICTIONARY!!
# hero = {
#         "name": character_name,
#         "type": character_type,
#         "health": character_health,
#         "attack": character_strength
#     }
    
#     heroes.append(hero)

#4) Hero as a CLASS! I will not use it,because i only need 2 characters per battle, easier to do so with dictionary
# class Character:
#     def __init__(self, name, type_, health, attack):
#         self.name = name
#         self.type = type_
#         self.health = health
#         self.attack = attack

# heroes = []

# for i in range(2):
#     name, type_ = generate_character()
#     h = health()
#     a = attack()
#     hero = Character(name, type_, h, a)
#     heroes.append(hero)

# # dostęp:
# print(heroes[0].name, "vs", heroes[1].name)
# print(heroes[0].name, "has", heroes[0].health, "HP")

#Day 28 - BATTLE GAME - utilizing code from 27th day
import random
import string
import time
import os

def random_name(length=6):
  return ''.join(random.choice(string.ascii_letters) for _ in range(length))

names_list = ["Aiden", "Aria","Myrola", "Bura", "Temar", "Hikaru", "Jolin", "Mikaku"]
types_list = ["human", "imp", "wizard", "elf", "orc", "shrek", "angel"]

def generate_character():
  name = random.choice(names_list)
  type = random.choice(types_list)
  return name, type

def rollDice(sides):
  sides = random.randint(1,sides)
  return sides

def health():
  health = ((rollDice(6) * rollDice (12))/2)+ 10
  return health

def attack():
  attack = ((rollDice(6) * rollDice (12))/2)+ 12
  return attack

def isAlive():
  return 

time.sleep(1)
print("CHARACTER BUILDER")
continue_building = "yes"

heroes = []

while True:
  heroes = []
  dice = []
  damage = 0
  
  for i in range(2):
    character_name,character_type = generate_character()
    character_health = health()
    character_strength = attack()

    hero={
      "name": character_name,
      "type": character_type,
      "health": character_health,
      "attack": character_strength
    }
    heroes.append(hero)
  
    print("You character is ", heroes[i]["name"])
    print("character TYPE: ", heroes[i]["type"])
    print(character_name, "health points: ", heroes[i]["health"])
    print(character_name, "attack stats: ", character_strength)
    print()

  print("Battle scene here:")
  if dice[0] > dice[1]:
    print("Hero ", heroes[0]["name"], " wins this round!")
    damage = abs(heroes[0]["health"] - heroes[1]["health"])
    heroes[1]["health"] -= (damage+1)
    if heroes[1]["health"] <= 0:
      print("HERO ", heroes[0]["name"], " you have won!" )
      break
  elif dice[0]==dice[1]:
    print("we have a TIE! No points!")
  else:
    #dice[0]<dice[1]
    print("Hero ", heroes[1]["name"], " wins this round!")
    damage = abs(heroes[1]["health"] - heroes[0]["health"])
    heroes[0]["health"] = heroes[0]["health"] - (damage+1)
    if heroes[0]["health"] <= 0:
      print("HERO ", heroes[0]["name"], " you have won!" )
      break
  
  # time.sleep(3)
  # os.system("clear")
  print("Status check:")
  #check if no
  print(heroes[0]["name"], "has health: ", heroes[0]["health"])
  print(heroes[1]["name"], "has health: ", heroes[1]["health"])
    
  continue_building = input("Do you want to continue? >")
  if continue_building == "yes" or continue_building == "Yes":
    os.system("clear")
    continue
  else:
    break

print("You've created many awesome characters today! See you!")


# THE OTHER SOLUTION:import random, os, time

# def rollDice(side):
#   result = random.randint(1,side)
#   return result

# def health():
#   healthStat = ((rollDice(6)*rollDice(12))/2)+10
#   return healthStat

# def strength():
#   strengthStat = ((rollDice(6)*rollDice(8))/2)+12
#   return strengthStat


# print("⚔️ BATTLE TIME ⚔️")
# print()
# c1Name = input("Name your Legend:\n")
# c1Type = input("Character Type (Human, Elf, Wizard, Orc):\n")
# print()
# print(c1Name)
# c1Health = health()
# c1Strength = strength()
# print("HEALTH:", c1Health)
# print("STRENGTH:", c1Strength)
# print()
# print("Who are they battling?")
# print()

# c2Name = input("Name your Legend:\n")
# c2Type = input("Character Type (Human, Elf, Wizard, Orc):\n")
# print()
# print(c2Name)
# c2Health = health()
# c2Strength = strength()
# print("HEALTH:", c2Health)
# print("STRENGTH:", c2Strength)
# print()

# round = 1
# winner = None

# while True:
#   time.sleep(1)
#   os.system("clear")
#   print("⚔️ BATTLE TIME ⚔️")
#   print()
#   print("The battle begins!")

#   c1Dice = rollDice(6)
#   c2Dice = rollDice(6)

#   difference = abs(c1Strength - c2Strength) + 1

#   if c1Dice > c2Dice:
#     c2Health -= difference
#     if round==1:
#       print(c1Name, "wins the first blow")
#     else:
#       print(c1Name, "wins round", round)
#   elif c2Dice > c1Dice:
#     c1Health -= difference
#     if round==1:
#       print(c2Name, "wins the first blow")
#     else:
#       print(c2Name, "wins round", round)
#   else:
#     print("Their swords clash and they draw round", round)

#   print()
#   print(c1Name)
#   print("HEALTH:", c1Health)
#   print()
#   print(c2Name)
#   print("HEALTH:", c2Health)
#   print()

#   if c1Health<=0:
#     print(c1Name, "has died!")
#     winner = c2Name
#     break
#   elif c2Health<=0:
#     print(c2Name, "has died!")
#     winner = c1Name
#     break
#   else:
#     print("And they're both standing for the next round")
#     round += 1
    

# time.sleep(1)
# os.system("clear")
# print("⚔️ BATTLE TIME ⚔️")
# print()
# print(winner, "has won in", round, "rounds")