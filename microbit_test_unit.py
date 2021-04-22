import pygame
import serial
import microbit_serial as ubit
from threading import Thread
import sys
import time

width = 800
height = 800
data = [0, 0, 0, 0]
timer = 0

# Init pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))

# Connect to the microbit
port = ubit.connect()
while type(port) is not serial.Serial:
    print("Looking for a microbit")
    run_notice = True
    port = ubit.connect()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
print("Microbit Found")
pygame.time.wait(200) # Let the OS setup the port
port.open()

def get_data():
    """
    This function is used to loop the retrieving of data
    from the microbit. It depends on microbit_serial
    functions.
    """
    global data
    try:
        if port.in_waiting > 0:
            # Obtain data from the microbit
            data = ubit.data(port)
            while type(data) != list: # Make sure message is intact and wait for it to come
                data = ubit.data(port)
            print(data)
            port.write("Y".encode()) # Let the microbit know we received the data
    except: # Controller disconnected
        data = [-1, -1, -1, -1]

def run_in_thread(func):
    """
    This function is used to run a function
    fun in a separate thread.
    - func: The function to run in a different thread.
    """
    thread = Thread(target=func)
    thread.daemon = True
    thread.start()

def draw_text(screen, text, X, Y):
    """
    This function draws any text to the screen.
    - screen: pygame.displayto draw to.
    - text: string of the text to draw.
    - X: x coordinate of the center of the text.
    - Y: y coordinate of the center of the text.
    """
    font = pygame.font.Font("dpcomic/dpcomic.ttf", 20)
    text_img = font.render(text, True, (255, 255, 255))
    text_rect = text_img.get_rect()
    text_rect.center = (X, Y)
    screen.blit(text_img, text_rect)
    return [text_img, text_rect]

def decrease_lives():
    """
    This function decreases by one the lives variable
    and sends an instruction to the microbit so that
    it turns off one LED.
    """
    try:
        lives -= 1
        port.write("D".encode())
    except: # Controller disconnected
        data = [-1, -1, -1, -1]

# Sync with the microbit
port.write("Y".encode())
# Reset lives
port.write("R".encode())
while True:
    # Scroll lives
    port.write("D".encode())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    run_in_thread(get_data)
    screen.fill((0, 0, 0))
    button = "Button press: "
    if data[0] == 1:
        button += "U"
    elif data[0] == 2:
        button += "L"
    elif data[0] == 3:
        button += "D"
    elif data[0] == 4:
        button += "R"
    pot = "Pot: {}".format(data[2])
    fan = "Fan: {}".format(data[3])
    draw_text(screen, button, int(width / 2), width / 4)
    draw_text(screen, pot, int(width / 2), (2 * (width / 4)))
    draw_text(screen, fan, int(width / 2), width - (width / 4))
    pygame.display.flip()