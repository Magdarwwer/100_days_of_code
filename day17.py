#Day 17 - BREAk & CONTINUE & EXIT
#BREAK - leaves the LOOP completely
#CONTINUE - still go on, but skip this example
#continue restarts the loop from the first line
#exit()- completely stops the programm
#1
# while True:
#   print("You are in a corridor, do you go left or right?")
#   direction = input("> ")
#   if direction == "left":
#     print("You have fallen to your death")
#     break

#2
# while True:
#   print("You are in a corridor, do you go left or right?")
#   direction = input("> ")
#   if direction == "left":
#     print("You have fallen to your death")
#     break
#   elif direction == "right":
#     continue
#   else:
#     print("Ahh! You're a genius, you've won")

#3
# while True:
#   print("You are in a corridor, do you go left or right?")
#   direction = input("> ")
#   if direction == "left":
#     print("You have fallen to your death")
#     break
#   elif direction == "right":
#     continue
#   else:
#     print("Ahh! You're a genius, you've won")
#     exit()
# print("The game is over, you've failed!")

# #4 fix code challenge:
# print("Let's play chutes and ladders. Pick ladder or chute.")
# while True:
#   print("Do you want to go up the ladder or down the chute?")
#   direction = input("> ")
#   if direction == "chute":
#     print("Game over!")
#     break
#   elif direction == "ladder":
#     continue
#   else:
#     print("Game over!")
#     exit()
# print("Thanks for playing!")


#5 - daily challenge: utlilizing code from day 14
# repreating the game for multiple rounds:
from getpass import getpass as input

counterP1 = 0
counterP2 = 0

print("E P I C 🪨  📄 ✂️ B A T T L E")
while True:
  play_again = input("Want to play another round? >")
  if play_again == "yes":
    print("Select your move (R, P or S)")
    p1 = input("Player 1 > ")
    p2 = input("Player 2 > ")
  
    if p1 == p2:
      print("Tie, no points")
    elif p1 == "S" and p2 == "P":
      print("Player 1 Scizzors cuts Player 2 Paper")
      counterP1 += 1
      if counterP1 == 3:
        print("Player 1 wins!")
      elif counterP2 == 3:
        print("Player 2 wins!")
      elif counterP1 > counterP2:
        print("Player 1 is winning with ",counterP1, "points")
      elif counterP2 == counterP1:
        print("TIE!")
      else:
        print("Player 2 is winning with ",counterP2, "points")
    elif p1 == "R" and p2 =="S":
      print("Player 1 Rock cuts Player 2 Scizzors")
      counterP1 += 1
      if counterP1 == 3:
        print("Player 1 wins!")
        exit()
      elif counterP2 == 3:
        print("Player 2 wins!")
        exit()
      elif counterP1 > counterP2:
        print("Player 1 is winning with ",counterP1, "points")
        continue
      elif counterP2 == counterP1:
        print("TIE!")
        continue
      else:
        print("Player 2 is winning with ",counterP2, "points")
        continue
    elif p1 == "P" and p2 == "R":
      print("Player 1 Paper cuts Player 2 Rock")
      counterP1 += 1
      if counterP1 == 3:
        print("Player 1 wins!")
        exit()
      elif counterP2 == 3:
        print("Player 2 wins!")
        exit()
      elif counterP1 > counterP2:
        print("Player 1 is winning with ",counterP1, "points")
        continue
      elif counterP2 == counterP1:
        print("TIE!")
        continue
      else:
        print("Player 2 is winning with ",counterP2, "points")
        continue
    elif p2 == "S" and p1 == "P":
      print("Player 2 Scizzors cuts Player 1 Paper")
      counterP2 += 1
      if counterP1 == 3:
        print("Player 1 wins!")
        exit()
      elif counterP2 == 3:
        print("Player 2 wins!")
        exit()
      elif counterP1 > counterP2:
        print("Player 1 is winning with ",counterP1, "points")
        continue
      elif counterP2 == counterP1:
        print("TIE!")
        continue
      else:
        print("Player 2 is winning with ",counterP2, "points")
        continue
    elif p2 == "R" and p1 =="S":
      print("Player 2 Rock > Player 1 Scizzors")
      counterP2 += 1
      if counterP1 == 3:
        print("Player 1 wins!")
        exit()
      elif counterP2 == 3:
        print("Player 2 wins!")
        exit()
      elif counterP1 > counterP2:
        print("Player 1 is winning with ",counterP1, "points")
        continue
      elif counterP2 == counterP1:
        print("TIE!")
        continue
      else:
        print("Player 2 is winning with ",counterP2, "points")
        continue
    elif p2 == "P" and p1 == "R":
      print("p2 PAPER > p1 Scizzors")
      counterP2 += 1
      if counterP1 == 3:
        print("Player 1 wins! with ", counterP1, " points!")
        exit()
      elif counterP2 == 3:
        print("Player 2 wins! with ", counterP2, " points!")
        exit()
      elif counterP1 > counterP2:
        print("Player 1 is winning with ",counterP1, "points")
        continue
      elif counterP2 == counterP1:
        print("TIE!")
        continue
      else:
        print("Player 2 is winning with ",counterP2, "points")
        continue
    else:
      print("Something went wrong")