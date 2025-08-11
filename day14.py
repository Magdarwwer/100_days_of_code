#Day 14 - rock paper scizors:
# palyer 1 and palyer 2 -> ask both for an input
# input and output,
# if/elif/else statements,
# basic mathematics,
# and casting as float and int.
from getpass import getpass as input

print("E P I C 🪨  📄 ✂️ B A T T L E")
print("Select your move (R, P or S)")
p1 = input("Player 1 > ")
p2 = input("Player 2 > ")

if p1 == p2:
  print("Tie, no points")
elif p1 == "S" and p2 == "P":
  print("Player 1 Scizzors cuts Player 2 Paper")
elif p1 == "R" and p2 =="S":
  print("Player 1 Rock cuts Player 2 Scizzors")
elif p1 == "P" and p2 == "R":
  print("Player 2 Paper cuts Player 1 Rock")
elif p2 == "S" and p1 == "P":
  print("Player 2 Scizzors cuts Player 1 Paper")
elif p2 == "R" and p1 =="S":
  print("Player 2 Rock > Player 1 Scizzors")
elif p2 == "P" and p1 == "R":
  print("p2 PAPER > p1 Scizzors")
else:
  print("Something went wrong")
#--------another version----
# from getpass import getpass as input

# print("E P I C    🪨  📄 ✂️    B A T T L E ")
# print()
# print("Select your move (R, P or S)")
# print()

# player1Move = input("Player 1 > ")
# print()
# player2Move = input("Player 2 > ")
# print()

# if player1Move=="R":
#   if player2Move=="R":
#     print("You both picked Rock, draw!")
#   elif player2Move=="S":
#     print("Player1 smashed Player2's Scissors into dust with their Rock!")
#   elif player2Move=="P":
#     print("Player1's Rock is smothered by Player2's Paper!")
#   else:
#     print("Invalid Move Player 2!")
# elif player1Move=="P":
#   if player2Move=="R":
#     print("Player2's Rock is smothered by Player1's Paper!")
#   elif player2Move=="S":
#     print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
#   elif player2Move=="P":
#     print("Two bits of paper flap at each other. Dissapointing. Draw.")
#   else:
#     print("Invalid Move Player 2!")
# elif player1Move=="S":
#   if player2Move=="R":
#     print("Player 2's Rock makes metal-dust out of Player1's Scissors")
#   elif player2Move=="S":
#     print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
#   elif player2Move=="P":
#     print("Player1's Scissors make confetti out of Player2's paper!")
#   else:
#     print("Invalid Move Player 2!")
# else:
#   print("Invalid Move Player 1!")