#Custom affirmations generator - and not or:
name = input("What's your name? >" )
if name == "bob" or name == "Bob" and name != "al":
  print("everything's alright")
elif 'a' in name:
  print("there's a letter in your name")
else:
  print("Who are you? ")
  
