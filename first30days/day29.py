#Day 29 - all use cases of PRINT function, \n

# #1you can tell print what to do at the end
# for i in range(0, 100):
#   print(i, end=": ")
# #whatever you put in a quote the system will place it after (in the example) the number

# #2 \n
# for i in range(0,100):
#   print(i, end="\n")

# #3\t TAB
#   #2 \n
#   for i in range(0,100):
#     print(i, end="\t")

#\v Vertical Tab:
    #2 \n
# for i in range(0,100):
#   print(i, end="\v")
#we can use it 


#4
# # print("If you put")
# print("\033[33m", end="") #yellow
# print("nothing as the")
# print("\033[35m", end="") #purple
# print("end character")
# print("\033[32m", end="") #green
# print("then you don't")
# print("\033[0m", end="") #default
# print("get odd gaps")


#5 a lot of double spaces here
# print("If you put", "\033[33m", "nothing as the", "\033[35m", "end character", 
#       "\033[32m", "then you don't", "\033[0m", "get odd gaps", end="")

#6 sep - for SEPARATOR - but you need to add spaces in text yourself
# print("If you put ", "\033[33m", "nothing as the ", "\033[35m", "end character ", 
#       "\033[32m", "then you don't ", "\033[0m", "get odd gaps ", sep="")


#7Secret cursos - COMMAND TO TURN THE CURSOR OF
# import os, time

# #turn cursor off:
# #print("\033[?25l", end="")

# #turn cursor on:
# print("\033[?25h", end="")

# for i in range(1, 101):
#   print(i)
#   time.sleep(0.5)
#   os.system("clear")
#------------
# import os, time
# print('\033[?25l', end="")
# for i in range(1, 101):
#   print(i)
#   time.sleep(0.2)
#   os.system("clear")

# print('\033[?25h', end="")

#Day 29 challenge - Write a subroutine
# color, and text as argument
# print text in that color and turn
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


print("Super Subroutine")
print("With my ", end="")
changeColor("purple", "new program")
changeColor("reset", " I can just call red( 'and') ")
changeColor("red", "it will print in red ")
changeColor("blue", "or even blue\n ")
changeColor("no", "With no ")
changeColor("cyan", "weird gaps\n")
changeColor("re", "EPIC.")

