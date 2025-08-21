#Day 30 - format string | f-string: the newest thing in python of outputting variables | ALIGNMENt <>
#and text together
#f-strings (format strings) are the best way to combine variables and text together.
#f-string allows you to write whole paragraphs of text and 
#explicitly state we want variables to go in that particular order.
name = "Katie"
age = "28"
pronouns = "she/her"

print("1)This is", name, "using", pronouns, "pronouns and is age", age)

print("----------------")
print("2)This is {}, using {} pronouns, and is {} years old.".format(name, pronouns, age))

#----------------
print(f"3)This is {name}, using {pronouns} pronouns, and is {age} years old.")
#--------

#WE can SET local variables within the f-string itself. Now it doesn't 
#matter the order of the variables. format.( = )
print("""4) This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, 
{name}.How are you? Have you been having a great {age} years so far"""
      .format(pronouns=pronouns, name=name, age=age))

#f-strings work with different variable types too: int, float, and string.

#5) We can assign concatenated sentences to variables:
response = "5)This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far".format(name=name, pronouns=pronouns, age=age)

print(response)

#Alignment: left = <, right = >, center = ^
# for i in range(1, 31):
#   print(f"Day {i} of 30")

#2:Let's fix the missalignment by adding a left alignment of 2 characters long. 
#The sign < creates a gap of that many characters and aligns the text inside
# for i in range(1, 31):
#   print(f"Day {i: <2} of 30")

#{variable: <2}
# #Common errors:
# for i in range(1, 31):
#   print(f"Day {i: <2} of 100")

#another form:
# for i in range(1, 31):
#   print("Day {count} of 100".format(count=i))

#FIX MY CODE :
food = "pizza"
location = "beach"
color = "green"
friend = "Quinn"

response = "Alejandra ordered {food} to eat at the {location} with her friend, {friend}. She got to the {location} and looked for a {color} umbrella where {friend} said they would be waiting. By the time, Sally found {friend}, the {food} was cold and the {location} was lame.".format(food=food, friend = friend, location=location, color=color,)

print(response)

#Day 30 challenge:
