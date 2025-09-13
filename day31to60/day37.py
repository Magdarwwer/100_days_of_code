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
print(myString[::-1])
