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
  if(name == "strength"):
    print("  Woah, SO STRONG!!!")
    
#if statement 
myDictionary = {"name" : "David the Mildy Terrifying", "health": 186, "strength": 4, "equipped":"l33t haxx0r p0werz"}

for name,value in myDictionary.items():
  print(f"{name}:{value}")

  if (name == "strength"):
    if value > 100:
      print("Whoa, SO STRONG")
    else:
      print("Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!")