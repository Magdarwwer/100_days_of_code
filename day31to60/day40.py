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
#Place where you can store all info about one person
print("🌟Contact Card🌟")
username = input("Please enter your name >")
userbirth = input("Please enter your birthday")
userphonenumber = input("Please enter your telephone")
useremail = input("Please enter your email>").strip()
useraddres = input("Please enter your address >").strip()

newUser = {"name": username, "birthday": userbirth, "phonenumber": userphonenumber, "email": useremail, "address": useraddres}

print(newUser)

print(f'Hi {newUser["name"]}. The Dictionary says that you were born on {newUser["birthday"]}, we can call you on {newUser["phonenumber"]}, email {newUser["email"]}, or write to the {newUser["address"]}')

#THE OUTCOME FROM REPLIT
# Please enter your name >Magdalena
# Please enter your birthday30/09/2001
# Please enter your telephone678 594 394 
# Please enter your email>aaa@email.com
# Please enter your address >Keakow Poland
# {'name': 'Magdalena', 'birthday': '30/09/2001', 'phonenumber': '678 594 394', 'email': 'aaa@email.com', 'address': 'Keakow Poland'}
# Hi Magdalena. The Dictionary says that you were born on 30/09/2001, we can call you on 678 594 394, email aaa@email.com, or write to the Keakow Poland



#ANOTHER SOLUTION:
# name = input("Name: ").strip().capitalize()
# dob = input("Date of Birth: ").strip()
# tel = input("Telephone number: ").strip()
# email = input("Email: ")
# address = input("Address: ")
# contact = {"name": name, "dob": dob, "tel": tel, "email": email, "address": address}
# print()
# print(f"""Name: {contact["name"]}""")
# print(f"""DOB: {contact["dob"]}""")
# print(f"""Tel: {contact["tel"]}""")
# print(f"""Email: {contact["email"]}""")
# print(f"""Address: {contact["address"]}""")