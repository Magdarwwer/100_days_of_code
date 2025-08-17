# The key is that the Output tool is specifically for programs
# that produce multimedia output (audio/graphics), 
# while Console is for text input/output, and Preview is for web applications.
import os
import time
for i in range(1,1000):
  print(i)
  os.system("clear") # cleans the previous line

#2
print("Welocme")
print("To")
print("replit")

time.sleep(3) # pasues the program for the amount of seconds I put in

os.system("clear")

username = input("Username: ")