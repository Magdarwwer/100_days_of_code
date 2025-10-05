#Day 41 - dictionaries & loops

#dictionaries stores two bits of data - why two bits
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

for i in myDictionary:
  print(myDictionary[i])
  
print()
print("KEYS:")
for i in myDictionary:
  print(i)


#printig values again:
print()
print("VALUES:")
for value in myDictionary.values():
  print(value)


#printing both:
for name, value in myDictionary.items():
  print(f"{name}:{value}")