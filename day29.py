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


#7Secret cursos