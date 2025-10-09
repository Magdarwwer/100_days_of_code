#Day42 - 
pokemonTypes = ["fire", "water", "earth", "wind", "magical", "szkorpon"]
pokedict = {"name": None, "type": None, "special move": None, "HP": None, "MP":None }

def checkPokeType(ptype):
    if ptype == "fire":
      return "\033[31m"
    elif ptype == "water":
      return "\033[34m"
    elif ptype == "earth":
      return "\033[32m"
    elif ptype == "wind":
      return "\033[37m"
    elif ptype == "magical":
      return "\033[35m"
    elif ptype == "szkorpon":
      return "\033[36m"
    else:
      return "\033[37m"

for name in pokedict.keys():
  pokedict[name] = input(f"Input your beast's {name} > \t").strip().lower()

#save color to print all dictionary parts in
color = checkPokeType(pokedict["type"])

print("--------")
print(color, end="")

for name, value in pokedict.items():
    #if name == "type":
        #checkPokeType(value)
    print(f"{name:<15}:{value}")
    
# Reset koloru po wypisaniu
print("\033[0m")


#ALTERNATIVE SOLUTION: COMMENT OUT
mokedex = {"Beast Name": None, "Type": None, "Special Move": None, "HP": None, "MP": None}

print("MokéBeast")
print()

for name, value in mokedex.items():
  mokedex[name] = input(f"{name}:\t").strip().title()

if mokedex["Type"]=="Earth":
  print("\033[32m", end="")
elif mokedex["Type"]=="Air":
  print("\033[37m", end="")
elif mokedex["Type"]=="Fire":
  print("\033[31m", end="")
elif mokedex["Type"]=="Water":
  print("\033[34m", end="")
else:
  print("\033[33m", end="")

for name, value in mokedex.items():
  print(f"{name:<15}: {value}")

