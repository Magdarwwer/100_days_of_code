#Day 40- Dictionaries

#lists are accesed by numeric numbers, not randomly -> no connection between 
#value & key - ex. job <-> name .... DO YOU REMEMBER the name of assistant? -> John <- NO INDEXES
myUser = {"name" : "David", "age": 128}
print(myUser["name"])
print(myUser["job"])

print(myUser)
print(f'Your name is {myUser["name"]} and your age is {myUser["age"]}')

#double "" -> is a string
#double '' -> is a string
#BUT THEY HAVE TO MATCH! fixed upper f-string print line

# THATS WRONG
# # myUser = {name:"David", "age": 128, "age" = 129}
# print(myUser)

#Fix my code - task:
#fix my code:
myUser = {"name":"Andy", "age":128}
myUser["age"] = 129
print(myUser["name"])

#DAY 40challenge: Today's challenge is to create a contact card using a dictionary.
