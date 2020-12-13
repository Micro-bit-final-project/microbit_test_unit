# Allow importing a file outside of python path
import sys, os
sys.path.append("../")
# Import microbit serial handler
from microbit_serial import microbit_serial as ubit

import pygame, serial
from time import sleep

# Init pygame
pygame.init()

# Window set up
screen = pygame.display.set_mode([800, 800])
background = 30, 30, 30
screen.fill(background)

# Connect to the microbit
port = ubit.connect()
while type(port) is not serial.Serial:
    print("Looking for a microbit")
    port = ubit.connect()
    sleep(1)

print("Microbit Found")

run = True
while run:
    for event in pygame.event.get():
        # Run forever until user presses X to close the window
        if event.type == pygame.QUIT:
            run = False
            break

# Quit game
pygame.quit()
sys.exit()