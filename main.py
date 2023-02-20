import pygame

# Intialize PyGame
pygame.init()

# Sets the screen size to a width of 800px and height to 600px
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("GalagaCIS293 BY SHAWN, TAYLOR AND CODY")
icon = pygame.image.load('GALAGATSC.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
#positions the player icon
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg,(playerX,playerY))

# Greate game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # RGB Screen colors
    screen.fill((21, 40, 71))
    player()
    #updates the display with the color
    pygame.display.update()