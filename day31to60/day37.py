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
new_second_name = maiden_name[0:2].capitalize() + city[0:3].lower()

print(
    f"Your new Star Wars name: May the force be with you {new_first_name} {new_second_name}!"
)

#SECOND SOLUTION USING SPLI!!! Extra points for getting all the inputs with just one input command and the split function.
all_in_one = input(
    "Enter first name, last name, maiden name and the city separated with a SPACE >"
)
new_list = all_in_one.split()

new_name = new_list[0][:3].title() + new_list[1][:3].lower()
new_last_n = new_list[2][:2].capitalize() + new_list[3][:3].lower()

final_name = new_name + " " + new_last_n
print(final_name)
print(f"May the force be with you {final_name}")


#TIPS:
#1) To get charaters from the beginning of a string, leave the first argument blank. ex: [:3] gets the first 3 characters.
#2) To get charaters from the end of a string, make the first argument a negative number for how many charaters to get. Leave the last argument blank. ex: [-5:] gets the last 5 characters.
#3) fString formatting uses .title for first character capitalization and .lower for all lower case.
#4) Use fStrings to join the sliced characters to a new variable as you get the correct characters from each string.
#5) For extra points, get the user to input all info at once separated by spaces.