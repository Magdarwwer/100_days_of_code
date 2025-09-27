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