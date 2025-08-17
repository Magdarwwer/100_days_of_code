# The key is that the Output tool is specifically for programs
# that produce multimedia output (audio/graphics), 
# while Console is for text input/output, and Preview is for web applications.
# import os
# import time
# for i in range(1,1000):
#   print(i)
#   os.system("clear") # cleans the previous line

# #2
# print("Welocme")
# print("To")
# print("replit")

# time.sleep(3) # pasues the program for the amount of seconds I put in

# os.system("clear")

# username = input("Username: ")

#part 2 Daily challenge:
#Day 26 - OS library + TIME LIBARRY
#os library let's you talk to the console
#Challenge 26 - BUILD menu, use while True - make old iPod:
import os
import time

import pygame
import sys

# Force pygame to use ALSA audio driver
import os
os.environ['SDL_AUDIODRIVER'] = 'alsa'

pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=1024)
pygame.mixer.init()
pygame.init()

# Check if audio system is working
print("Pygame mixer initialized:", pygame.mixer.get_init())
print("Available audio drivers:", pygame.mixer.get_init())

sound = pygame.mixer.Sound('audio.wav')
print("Audio file loaded successfully")

# Force immediate audio playback
print("Starting audio playback to trigger Output tool...")
channel = sound.play()
print("Audio channel:", channel)
time.sleep(2)
sound.stop()
print("If you can hear audio, the Output tool should have appeared")

def pause():
  pygame.mixer.pause()

def play():
  sound.play(-1)  # -1 means loop indefinitely

def stop():
  pygame.mixer.stop()

def show_menu():
  print("🎵 My iPod Menu 🎵")
  print("1. Play")
  print("2. Pause")
  print("3. Stop")
  print("4. Exit")
  print()

while True:
  os.system("clear")
  show_menu()

  choice = input("Enter your choice (1-4): ")

  if choice == "1":
    print("▶️ Playing music...")
    play()
    time.sleep(2)
  elif choice == "2":
    print("⏸️ Pausing music...")
    pause()
    time.sleep(2)
  elif choice == "3":
    print("⏹️ Stopping music...")
    stop()
    time.sleep(2)
  elif choice == "4":
    print("👋 Goodbye!")
    stop()
    break
  else:
    print("❌ Invalid choice! Please try again.")
    time.sleep(2)