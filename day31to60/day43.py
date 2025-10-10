#Day 43 - Tables/ 2D DIMENTIONAL LISTS
#ertical data is used for fields: one category - name, ID, favorite biscuit, etc
#Behind the scenes, we see a list inside a list
import random
my1DList = ["Johnny", 21, "Mac"]

my2DList = [ ["Johnny", 21, "Mac"],
             ["Sian", 19, "PC"],
             ["Gethin", 17, "PC"] ]

my2DList = [ ["Johnny", 21, "Mac"], ["Sian", 19, "PC"], ["Gethin", 17, "PC"] ]

print(my2DList) # This will output [['Johnny', 21, 'Mac'], ['Sian', 19, 'PC'], ['Gethin', 17, 'PC']]


#to print a single row:
print(my2DList[0])# This code outputs ['Johnny', 21, 'Mac'].

print(my2DList[0][0]) # This code outputs 'Johnny'. It's Johnny's name from list 0 (first square bracket), item 0 (second square bracket)

print(my2DList[1][2]) # This code outputs 'PC'. It's Sian's computing preferene from list 1 (first square bracket), item 2 (second square bracket)

#playing out with changing elements in 2D lists:
my2DList[1][2] = "Linux"

print(my2DList[1])
print(my2DList)

#COMMON ERRORS:
my2DList = [ ["Johnny", 21, "Mac"],
             ["Sian", 19, "PC"],
             ["Gethin", 17, "PC"] ]
print(my2DList[0][2])


#FIX MY CODE:
my2DList =[  ["Johnny", 21, "Mac"], # No opening square bracket
             ["Sian", 19, "PC"],    #Missing two commas one after "Sian" and one after a line
             ["Gethin", 17, "PC"] ] #Extra , after this sub list - the last sub-list doesn't have a comma after it.

print(my2DList[0][1])

#DAY43 - BINGO CARD with 2D lists:
#randomly generate numbers in a list
#fill in Bingo Card with random numbers
#display the Bingo Card

bingo2D = [[]]

for item in range(0,3):
    for jtem in range(0,3):
        number = random.randint(0,91)
        if item == 1 and jtem == 1:
            bingo2D[item][jtem] = "BINGO"
        else:
            bingo2D[item][jtem] = number
