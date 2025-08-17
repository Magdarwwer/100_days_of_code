#Funkcja random.randint(a, b) zwraca losową liczbę całkowitą w zakresie od a do b.
# Funkcja random.randrange(start, stop, step) istnieje – działa jak range(), ale wybiera losową liczbę.
# Funkcja random.choices(lista, k=n) pozwala wylosować kilka elementów.

# return f"{name} the {char_type}"
# To zwraca jeden string (łańcuch tekstowy).
# f"..." oznacza f-string (formatted string literal).

#Day27 - SUBROUTINE generating the characters
#character type and name of the character

#soubroutin dice rolls HEALTh
#2nd soubroutine
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

time.sleep(1)
print("CHARACTER BUILDER")
continue_building = "yes"

while continue_building:
  character_name,character_type = generate_character()
  character_health = health()
  character_strength = attack()

  print("You character is ", character_name)
  print("character TYPE: ", character_type)
  print(character_name, "health points: ", character_health)
  print(character_name, "attack stats: ", character_strength)
  print()

  continue_building = input("Do you want to continue? >")
  if continue_building == "yes" or continue_building == "Yes":
    os.system("clear")
    continue
  else:
    break

print("You've created many awesome characters today! See you!")


# while True:
#   print("⚔️ CHARACTER BUILDER ⚔️")
#   print()
#   name = input("Name your Legend:\n")
#   type = input("Character Type (Human, Elf, Wizard, Orc):\n")
#   print()
#   print(name)
#   print("HEALTH:", health())
#   print("STRENGTH:", strength())
#   print()
#   print("May your name go down in Legend…")
#   print()
#   again = input("Again?:\n")
#   if again=="No" or again=="no":
#     break
#   time.sleep(1)
#   os.system("clear")