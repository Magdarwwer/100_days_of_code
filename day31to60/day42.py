#Day42 - 
pokemonTypes = ["fire", "water", "earth", "wind", "magical", "szkorpon"]
pokedict = {"name": None, "type": None, "special move": None, "HP": None, "MP":None }

def checkPokeType(ptype):
  if ptype in pokemonTypes:
    if ptype == "fire":
      print("\033[31m", end="")
    elif ptype == "water":
      print("\033[34m", end="")
    elif ptype == "earth":
      print("\033[32m", end="")
    elif ptype == "wind":
      print("\033[37m", end="")
    elif ptype == "magical":
      print("\033[35m", end="")
    elif ptype == "szkorpon":
      print("\033[36m", end="")
    else:
      print("\033[37m", end="")
  else:
    print("Not a pokemon")

for name in pokedict.keys():
  pokedict[name] = input(f"Input your beast's {name} > \t").strip().lower()

print("--------")
for name, value in pokedict.items():
    if name == "type":
        checkPokeType(value)
    print(f"{name}:{value}")
    
# Reset koloru po wypisaniu
print("\033[0m")
