# Allow importing a file outside of python path
import sys, os
sys.path.append("../")
# Import microbit serial handler
from microbit_serial import microbit_serial as ubit

import pygame, serial
from time import sleep

# Connect to the microbit
port = ubit.connect()
while type(port) is not serial.Serial:
    print("Looking for a microbit")
    port = ubit.connect()
    sleep(1)

# Connect to the microbit
print("Microbit Found")
port.open()

# Init pygame
pygame.init()

# Window set up
screen = pygame.display.set_mode([800, 800])
background = 30, 30, 30
screen.fill(background)

# Load the microbit image
image = pygame.image.load("microbit.png")
image_rec = image.get_rect()

# Calculate x and y to draw the image
X = int(round((800 - 540) / 2, 0))
Y = int(round((800 - 440) / 2, 0))

image_rec.x = X
image_rec.y = Y


def map(x, in_min, in_max, out_min, out_max):
    """
    From https://www.arduino.cc/reference/en/language/functions/math/map/
    Re-maps a number from one range to another.
    That is, a value of fromLow would get mapped to toLow,
    a value of fromHigh to toHigh, values in-between to values in-between, etc.

    - value: the number to map.
    - fromLow: the lower bound of the value’s current range.
    - fromHigh: the upper bound of the value’s current range.
    - toLow: the lower bound of the value’s target range.
    - toHigh: the upper bound of the value’s target range.
    """
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

run = True
while run:
    for event in pygame.event.get():
        # Run forever until user presses X to close the window
        if event.type == pygame.QUIT:
            run = False
            break

    # Obtain data from the microbit
    data = ubit.data(port)
    if type(data) is list: # Make sure message is intact
        uBitX = data[0]
        if uBitX > 1000:
            uBitX = 1000
        elif uBitX < -1000:
            uBitX = -1000
        angle = map(uBitX, -1000, 1000, -90, 90)

        screen.fill(background)
        rotated_image = pygame.transform.rotate(image, angle)
        rotated_rec = rotated_image.get_rect(center = image_rec.center)
        screen.blit(rotated_image, rotated_rec)
        
    # Update screen
    pygame.display.flip()

# Quit game
pygame.quit()
sys.exit()
