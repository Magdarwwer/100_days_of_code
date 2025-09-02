#LISTS ARRAYS
#sometimes you don;t know how much data you need to store
myList = []
#index 0
myList[2] = "stuff"
#dily remindersa
timetable = []

timetable = ["Computer Science", "Math", "English", "Art", "Sport"]
print(timetable)
#tell the computer which index to print out!
print(timetable[2])

timetable = ["Computer Science", "Math", "English", "Art", "Sport"]
print(timetable[0])
print(timetable[1])
print(timetable[2])
print(timetable[3])
print(timetable[4])

timetable[4]= "Watch TV"

print(timetable[0])
print(timetable[1])
print(timetable[2])
print(timetable[3])
print(timetable[4])

#Lists & Loops:
timetable = ["Computer Science", "Math", "English", "Art", "Watch TV"]
for lesson in timetable:
  print(lesson)

tablenew = ["a", "b", "c", "d", "e"]
for char in tablenew:
  print(char)


#Common Errors:
#Remember, start counting from 0. The first color in the list, red, is index 0. not 1
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet"]
print(f"The first color is {colors[0]}")

#2: not 6 -> 5
#There is no index 6 because you need to start counting from 0. The 6th item in the list,
#violet, is index 5.
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet"]
print(f"The first color is {colors[5]}")