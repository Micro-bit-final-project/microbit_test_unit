import sys, pygame

# Init pygame
pygame.init()

# Window set up
screen = pygame.display.set_mode([800, 800])
background = 30, 30, 30
screen.fill(background)

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