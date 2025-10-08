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
      
#COMMON ERRORS:
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

#
for name, value in myDictionary.items():
  print(f"{name}, {value}")
  
  
  
#FIX My CODE:
myDictionary = {"name" : "David the Mildy Terrifying", "health": 186, "strength": 4, "equipped":"l33t haxx0r p0werz"}

for name, value in myDictionary.items():
  print(f"{name}:{value}")

  if (name == "strength"):
    if value > 100:
      print("Whoa, SO STRONG")
    else:
      print("Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!")


#Day41 CHALLENGE - Create a dictionary hat stores the following information about a website: name, URL, description and a star rating (out of 5).

web_name = input("Input the website name: ")
web_url = input("Input the URL: ")
web_description = input("Input a web description")
web_rate = input("Input the star rating out og 5 *****: ")
       
websitesDict = {"name": web_name, "URL":web_url, "description": web_description, "rating": web_rate}

for name, value in websitesDict.items():
  print(f"{name}, {value}")
  
  
  
#ALTERNATIVE SOLUTION day41 daily challenge
website = {"name": None, "url": None, "desc": None, "rating": None, "image":None}

for name in website.keys():
  #print(name)
  website[name] = input(f"{name}: ")

print()
for name, value in website.items():
   print(f"{name}: {value}")