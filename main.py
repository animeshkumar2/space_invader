import pygame
import random
import math

# initialize the pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# title and icon(icons from flaticons.com)
pygame.display.set_caption('SPACE INVADER')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# player image inside the screen

playerimg = pygame.image.load('space.png')
playerX = 370
playerY = 490
playerX_change = 0

# enemy image inside the screen
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

for i in range(6):
    enemyimg.append(pygame.image.load('ufo.png'))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(+.5)
    enemyY_change.append(40)

# bullet image inside the screen

bulletimg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 450
bulletY_change = .70
bullet_state = 'ready'

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
testX = 10
testY = 10


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y, j):
    screen.blit(enemyimg[j], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletimg, (x + 16, y + 10))


# collision distance
def iscollision(x1, x2, y1, y2):
    distance = math.sqrt(math.pow((x1 - x2), 2) + (math.pow((y1 - y2), 2)))
    if distance <= 27:
        return 'true'
    else:
        return 'false'


# game loop
running = True
while running:
    # set bacground color

    screen.fill((1, 0, 0))
    # screen boundries control for the enemy and player
    if playerX <= -10:
        playerX = -10
    elif playerX >= 748:
        playerX = 748
    for i in range(6):
        if enemyX[i] <= 0:
            enemyX_change[i] = +.4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 768:
            enemyX_change[i] = -.4
            enemyY[i] += enemyY_change[i]
        enemyX[i] += enemyX_change[i]
        enemy(enemyX[i], enemyY[i], i)
        # collision condition
        collision = iscollision(enemyX[i], bulletX, enemyY[i], bulletY)
        if collision == 'true':
            bulletY = 450
            bullet_state = 'ready'
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(50, 150)
            score_value += 1
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = +0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bullet_state == 'fire'
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    player(playerX, playerY)

    # bullet fire code
    if bulletY <= 0:
        bulletY = 450
        bullet_state = 'ready'

    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    show_score(testX, testY)
    pygame.display.update()
