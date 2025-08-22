#Day 31 challenge: USER INTERFACE:4\
    #use print statements & f-strings
    #No inputs from the user
    

#FIRST INTERFACE:
def changeColor(color, word):
 if color=="red":
    print("\033[31m", word, sep="", end="")
 elif color == "blue":
   print("\033[0;34m", word, sep="", end="")
 elif color == "green":
   print("\033[0;32m", word, sep="", end="")
 elif color == "brown":
   print("\033[0;33m", word, sep="", end="")
 elif color == "purple":
   print("\033[0;35m", word, sep="", end="")
 elif color == "cyan":
    print("\033[0;36m", word, sep="", end="")
 elif color == "yellow":
   print("\033[1;33m", word, sep="", end="")   
 else:
   print("\033[0m", word, sep="", end="")


changeColor(f"red", "=")
changeColor("none", "=")
changeColor("blue", "=")
changeColor("yellow", "Music App")
changeColor("blue", "=")
changeColor("none", "=")
changeColor("red", "=")
# print("\n")

print("\n🔥▶", )
