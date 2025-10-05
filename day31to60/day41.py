#Day 41 - dictionaries & loops

#dictionaries stores two bits of data - why two bits
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

for i in myDictionary:
  print(myDictionary[i])
  
print()
print("KEYS:")
for i in myDictionary:
  print(i)
