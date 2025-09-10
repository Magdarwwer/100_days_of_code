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