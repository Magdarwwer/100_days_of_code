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
 elif color == "pink":
  print("\033[1;31m", word, sep = "", end="")
 else:
   return("\033[0m")


changeColor("red", "=")
changeColor("none", "=")
changeColor("blue", "=")
changeColor("yellow", "Music App")
changeColor("blue", "=")
changeColor("none", "=")
changeColor("red", "=")
# print("\n")

title = f"{changeColor('red', "=")}{changeColor('white',"=")}{changeColor('blue',"=")}{changeColor('yellow',"Music App")}"

# print(f"{changeColor('white')}{"PREV":<35}")
# print(f"{changeColor('green')}{"NEXT":^35}")
# print(f"{changeColor('purple')}{"PURPLE":>35}")

print(f"{changeColor('white', "PREV")}")
# print(f"{changeColor('green',"NEXT":^35)}")
# print(f"{changeColor('purple')}{"PURPLE":>35}")

counter = 0

colors = []
colors.append("none")
colors.append("green")
colors.append("pink")

print("\n")

#to fix xddd wtf
print(f"🔥▶\t{changeColor("white", "Radio gaga")}Radio Gaga")
changeColor("yellow", "\tQueen")
print("\n")

#testing what \t does xd
# for i in range(0,7):
#  print(i, end="\t")
 
  