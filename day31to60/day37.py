#Day 37 - string slicing
# chopping text into parts 

#1)This code outputs the 'H' from 'Hello'
myString = "Hello there my friend."
print(myString[0])
print(myString[0:5])
print(myString[:11])
print(myString[6:11])
print(myString[12:])
#this below is bad:
print(myString[12:0])

#a whole string
print(myString[:])

#print every other letter:
print(myString[0:5:2])
#Default at the start ->0 | Default at the end ->last | letter and print every 2 letters
print(myString[::2])
#print every 3 letters:
print(myString[::3])

#This code reverses the string, outputting '.dneirf ym ereht olleH'
print(myString[::-2])
#print JUST BACKWARD every letter
print(myString[::-1])

#split lets us split a string into a list of individual words 
#by separating it at the space characters.
myString = "Hello there my friend."
print(myString.split())
#This code outputs ['Hello', 'there', 'my', 'friend.']

#Common mistakes:
myString = "Hello there my friend."
print(myString[0:5])
#fixed 4 -> 5 to print 'Hello' instead of 'Hell'

#The 0 in the third argument means 'move on 0 characters in the string each time'. 
#You've told it to print the same character again and again and again....

#The third argument should be at least 1.
myString = "Hello there my friend."
print(myString[0:4:1])

#Fix my code:
# This code should output 'Hello there'
print()
print("Fix My Code:")
myString = "Hello there my friend."
print(myString[0:11:1])

#Day 37 CHALLENGE: Generate Star Wars Names:
first_name = input("Enter first name >")
last_name = input("Enter last name >")
maiden_name = input("what's your maiden name? >")
city = input("Enter city you were born in >")

new_first_name = first_name[0:3].title() + last_name[:3].lower()
print(new_first_name)