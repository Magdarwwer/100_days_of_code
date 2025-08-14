# DAY 20 ! 1/5 of a challenge. What can you really do with a RANGE() function?

#define range in betwen numbers
# for i in range(100, 110):
#   print(i)

#-----------
# for i in range(1, 7):
#   print("Day", i)

#----------
# for i in range(1, 8):
#   print("Day", i)

# #----------------
# print("Thirteen Times Table")
# for i in range(1, 13):
#   print(i, "x 13 =", i * 13)

#----goes from 
# for i in range (0, 1000000, 25):
#   print(i)

#-----counts back to -1 
# for i in range(10, -2, -1):
#   print(i)
  
# range(START, END, INCREMENT SIZE)
#the defult is +1
# for i in range (10, 0, -1):
#   print(i)

#error fix:
# for i in range (20, 40, 1):
#   print(i)

#Day 20 challenge - FOR - generating a list of numbers:
print("List Generator")
print()
print()
start = int(input("Start at: >"))
end = int(input("End before: >"))
increment = int(input("Increment >"))

for i in range(start, end, increment):
  print(i)