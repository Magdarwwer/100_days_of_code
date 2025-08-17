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
    
##Day 26 - OS library + TIME LIBARRY
#os library let's you talk to the console
#Challenge 26 - BUILD menu, use while True - make old iPod:
# import os
# import time

# import pygame
# import sys

# # Remove ALSA driver forcing - let pygame choose the best available driver
# try:
#     pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=1024)
#     pygame.mixer.init()
#     pygame.init()
    
#     # Check if audio system is working
#     print("Pygame mixer initialized:", pygame.mixer.get_init())
    
#     # Try to load the audio file
#     try:
#         sound = pygame.mixer.Sound('audio.wav')
#         print("Audio file loaded successfully")
        
#         # Force immediate audio playback
#         print("Starting audio playback to trigger Output tool...")
#         channel = sound.play()
#         print("Audio channel:", channel)
#         time.sleep(2)
#         sound.stop()
#         print("✅ Audio system working! Output tool should appear.")
        
#     except pygame.error as e:
#         print(f"❌ Could not load audio file: {e}")
#         print("Creating a simple beep instead...")
        
# except pygame.error as e:
#     print(f"❌ Audio initialization failed: {e}")
#     print("Audio features will be disabled")
#     sound = None


# def pause():
#   if sound:
#     pygame.mixer.pause()
#   else:
#     print("❌ Audio not available")


# def play():
#   if sound:
#     sound.play(-1)  # -1 means loop indefinitely
#   else:
#     print("❌ Audio not available")


# def stop():
#   if sound:
#     pygame.mixer.stop()
#   else:
#     print("❌ Audio not available")


# def show_menu():
#   print("🎵 My iPod Menu 🎵")
#   print("1. Play")
#   print("2. Pause")
#   print("3. Stop")
#   print("4. Exit")
#   print()


# while True:
#   os.system("clear")
#   show_menu()

#   choice = input("Enter your choice (1-4): ")

#   if choice == "1":
#     print("▶️ Playing music...")
#     play()
#     time.sleep(2)
#   elif choice == "2":
#     print("⏸️ Pausing music...")
#     pause()
#     time.sleep(2)
#   elif choice == "3":
#     print("⏹️ Stopping music...")
#     stop()
#     time.sleep(2)
#   elif choice == "4":
#     print("👋 Goodbye!")
#     stop()
#     break
#   else:
#     print("❌ Invalid choice! Please try again.")
#     time.sleep(2)

import pygame
import numpy as np
import wave

# Create a simple beep sound
def create_beep(filename, frequency=440, duration=3, sample_rate=22050):
    # Generate sine wave
    frames = int(duration * sample_rate)
    arr = np.sin(2 * np.pi * frequency * np.linspace(0, duration, frames))
    
    # Normalize to 16-bit range
    arr = (arr * 32767).astype(np.int16)
    
    # Write to WAV file
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)  # mono
        wav_file.setsampwidth(2)  # 2 bytes per sample
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(arr.tobytes())

create_beep('audio.wav')
print("Created audio.wav - a 3-second beep at 440Hz")

#to look again to fix:
import os
import time

import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')
sound.play()
pygame.mixer.pause()

def pause():
  pygame.mixer.pause()

pause()

def play():
  # Play the sound
  pygame.mixer.unpause()
  while True:
    stop_playback = int(input("Press 2 anytime to pause playback and go back to the menu: "))
    if stop_playback == 2:
      pause()
      return  # let's go back from this play() subroutine
    else:
      continue

while True:
  os.system("clear")
  print("🎵 MyPOD Music Player ")
  time.sleep(1)
  print("Press 1 to Play")
  print("Press 2 to Exit")
  print("Press anything else to see the menu again")
  userInput = int(input())
  if userInput == 1:
    print("Playing some proper tunes!")
    play()
  elif userInput == 2:
    exit()
  else:
    continue