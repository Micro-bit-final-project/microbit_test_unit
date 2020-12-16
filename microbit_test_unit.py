# Allow importing a file outside of python path
import sys, os
sys.path.append("../")
# Import microbit serial handler
from microbit_serial import microbit_serial as ubit

import pygame, serial
from time import sleep
from random import randint

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
send = False
while run:
    for event in pygame.event.get():
        # Run forever until user presses X to close the window
        if event.type == pygame.QUIT:
            run = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                send = True

    # Obtain data from the microbit
    data = ubit.data(port)
    while type(data) != list: # Make sure message is intact and wait for it to come
        data = ubit.data(port)
    print(data)

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
    if send:
        port.write("R".encode()) # Let the microbit know we are going to send data
    else:
        port.write("Y".encode()) # Let the microbit know we received the data

    # Update screen
    pygame.display.flip()

    if send:
        while True:
            message = port.readline().decode("utf-8")
            if message.find("Y") > -1:
                print("Ready")
                break

        # Send data to the microbit
        brightness_led_one = randint(0, 5)
        brightness_led_two = randint(0, 5)
        brightness_led_three = randint(0, 5)
        brightness_led_four = randint(0, 5)
        brightness_led_five = randint(0, 5)
        info = str([brightness_led_one, brightness_led_two, brightness_led_three, brightness_led_four, brightness_led_five])
        length = str(len(info))
        if len(length) < 3:
            if len(length) == 1:
                length = "0" + "0" + length
            elif len(length) == 2:
                length = "0" + length
        port.write(length.encode())
        print(length)

        while True:
            message = port.readline().decode("utf-8")
            if message.find("Y") > -1:
                print("Ready")
                break

        port.write(info.encode())
        print(info)

        # Obtain data from the microbit
        data = ubit.data(port)
        while type(data) != list: # Make sure message is intact and wait for it to come
            data = ubit.data(port)
        print(data)

        while True:
            message = port.readline().decode("utf-8")
            if message.find("Y") > -1:
                print("Ready")
                break
        send = False

# Quit game
pygame.quit()
sys.exit()
