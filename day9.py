#casting 
#Casting is where we explicitly tell the 
#computer that what we are typing is a number and not a letter.

#EXERCISES:
#1) SCORE:
#myScore = int(input("Your score: "))
#if myScore > 100000:
#  print("Winner!")
#else:
#  print("Try again 😭")

# 2)My Pi:
# myPi = float(input("What is Pi to 3dp?"))
# if myPi == 3.142:
#   print("Excatly")
# else:
#   print("Try again")

#common errors:
# - not being careful with brackets

#DAY 9 - challenge:
#GENERATION IDENTIFYIER:
import datetime

usersYear = int(input("Which year were you born? >"))
if usersYear < 1883:
    print("You're dead...RIP")
elif usersYear >=1883 and usersYear <= 1900:
    print("Lost Generation")
elif usersYear >1900 and usersYear <= 1927:
    print("Greatest generation")
elif usersYear > 1927 and usersYear <= 1945:
    print("Silent Generation")
elif usersYear > 1945 and usersYear <= 1964:
    print("Baby Boomers")
elif usersYear > 1964 and usersYear <= 1980:
    print("GEN X")
elif usersYear > 1980 and usersYear <= 1996:
    print("Millenials")
elif usersYear > 1997 and usersYear <= 2012:
    print("GEN Z")
elif usersYear > 2012 and usersYear <= datetime.date.today().year:
    print("gen Alpha")
else:
    print("You can't be born in the future")

# # Pobranie aktualnej daty
# dzisiaj = datetime.date.today()
# # Pobranie aktualnej daty i godziny
# teraz = datetime.datetime.now()

# # Pobranie roku z obiektu daty
# rok_z_daty = dzisiaj.year
# # Pobranie roku z obiektu datetime
# rok_z_datetime = teraz.year