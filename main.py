import pygame
import random
import math

# Intialize PyGame
pygame.init()

# Sets the screen size to a width of 800px and height to 600px
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("GALAGABG.png")

# Title and Icon
pygame.display.set_caption("GalagaCIS293 BY SHAWN, TAYLOR AND CODY")
icon = pygame.image.load('GALAGATSC.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
enemyImg = pygame.image.load("enemy.png")
bulletImg = pygame.image.load("bullet.png")

# positions the player icon
playerX = 370
playerY = 480
playerX_change = 0

# Enemy position and values
enemyX = random.randint(0, 735)
enemyY = random.randint(50, 150)
enemyX_change = 2
enemyY_change = 40

# Bullet position and values
# Ready state- unable to see on screen
# Fire state - the bullet it moving

bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

score = 0
def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def bullet(x, y):
    screen.blit(bulletImg, (x, y))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Greate game loop
running = True
while running:
    screen.fill((0, 0, 0))  # RGB Screen colors
    # set background image
    screen.blit(background, (0, 0))

    # The loop for the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Changes the position of the spaceship
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    #collision
    collision = isCollision(enemyX,enemyY,bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state ="ready"
        score += 1
        print(score)
        enemyX = random.randint(0,735)
        enemyY = random.randint(50,150)


    # setting the boundaries for the moment
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -3
        enemyY += enemyY_change

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()  # updates the display
