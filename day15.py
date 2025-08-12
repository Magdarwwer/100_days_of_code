# counter = 0
# while counter > 6:
#   print(counter)
#   counter += 1
#2---------------
# exit = ""
# while exit != "yes":
#   print("🥳")
#   exit = input("Exit?: ")
# #3------------------
# counter = 0
# while counter < 25:
#   print(counter)
#   counter += 1
#4-----------------
# counter = 0
# while counter <= 12:
#   print(counter)
#   counter += 1
#5------------------

exit = "no"

while exit != "yes":
  animal_sound = input("What animal do you want?: >") 
  if animal_sound == "cow" or animal_sound == "Cow":
    print("A cow goes moo.")
  elif animal_sound == "Cat":
    print("meow meow")
  elif animal_sound == "dog":
    print("hau hau")
  elif animal_sound == "eagle":
    print("AAAAAAAAAA")
  else:
    print("idk this animal lol")
    
  exit = input("Do you want to exit? >")

