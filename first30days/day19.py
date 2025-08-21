#Day 19 - FOR LOOP:
#1---------------
# counter = 0
# while counter < 10:
#   print(counter)
#   counter += 1

#2--------------
# for counter in range(10):
#   print(counter)

#pattern:
#for (variable) in range (number of values):
# The range function creates a list of numbers in the range you create. If you only give 
# # it one number, it will start at 0 
# # and move to a state where the final 
# #   number is one less than the number in the brackets. In this case, the 
# final number would be 9.
# total = 0
# for number in range(100):
#   total += number
#   print(total)

#-------------
# for days in range(7):
#   print("Day", days)

#-------------
# total = 10
# for counter in range(100):
#   total += 10
#   print(total)
#----------------
# total = 10
# for counter in range(100):
#   total += 10
#   print(total)


#Day 19 challenge:

print("LOAN CALCULATOR")
print()

amount = int(input("How much have you borrowed? >"))
years = int(input("In how many years would you like to pay the debt? >"))

procent = 0.05
current_debt = amount

for i in range (years):
  current_debt += (current_debt*procent)
  print("Year ", i+1 ," is ",round(current_debt, 2))

print("You paid ", round(current_debt - amount, 2)," in interest!")
  
# #another answer with set variables
# loan = 1000
# apr = 0.05
# for i in range(10):
#   loan+=(loan*apr)
#   print("Year", i+1, "is", round(loan,2))