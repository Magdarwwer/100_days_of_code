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