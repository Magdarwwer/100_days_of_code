print("Exam Grade Calculator")
print()
testName = input("Give the name of the test >")
print()
print("Name of exam: ", testName)
max_score = int(input("Give maxium score: >"))
score = int(input("Your score: > "))

#there's not always 100 points as a max
number_score = float(score/max_score)
final_number = round(number_score, 2)
final_perc =round(number_score*100,2)

print("You got",final_perc,"%")

# if score >= 100 and score > 89:
#   print("Wow you got an A+!")
#   print("You got ")
# elif score < 90 and score >= 80:
#   print("You got A- - good job")
# elif score < 80 and score > 69:
#   print("You've got a B")
# elif score < 70 and score > 59:
#   print("You've got a C")
# elif score < 60 and score > 50:
#   print("You've got a B")
# elif score < 50:
#   print("You've got a U")
  
#----------another version--------------
if final_number >= .90:
  print("Your letter score is an A+")
elif final_number >= .80 and final_number <= .89:
  print("Your letter grade is an A-.")
elif final_number >= .70 and final_number <= .79:
  print("Your letter score is a B.")
elif final_number >= .60 and final_number <= .69:
  print("Your letter grade is a C.")
elif final_number >= .50 and final_number <= .59:
  print("Your letter grade is a D.")
elif final_number <= .49:
  print("Your letter grade is a U.")
else: 
  print("Try again!")