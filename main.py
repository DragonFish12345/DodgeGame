import pygame
import time
import random

pygame.init()

# Creating Window
window = pygame.display.set_mode((800, 600))

# Setting Caption and Icon Image
pygame.display.set_caption('DodgeGame')
icon = pygame.image.load('Annotation 2020-08-20 122131.png')
pygame.display.set_icon(icon)

game_ended = False
winner = ''
running = True

# Stats
redrectstats = redrectx, redrecty, redrectw, redrectl = (250, 275, 50, 50)
bluerectstats = bluerectx, bluerecty, bluerectw, bluerectl = (500, 275, 50, 50)
circlecenter = circlex, circley = (400, 425)
circler = 25
circlev = 1
rectanglev = 1

# Images



def redwins():
    redrectwins = pygame.image.load('redrectwins.png')
    window.fill((0, 0, 0))
    window.blit(redrectwins, (0, 0))
    global winner
    global game_ended
    winner = 'red'
    game_ended = True


def bluewins():
    bluerectwins = pygame.image.load('bluerectwins.png')
    window.fill((0, 0, 0))
    window.blit(bluerectwins, (0, 0))
    global winner
    global game_ended
    winner = 'blue'
    game_ended = True

time.sleep(3)

while running:
    if not game_ended:
        window.fill((0, 0, 0))
        time.sleep(0.005)
        keys = pygame.key.get_pressed()

        randvx = random.randint(5, 10)
        randvy = random.randint(5, 10)
        randcx = random.randint(1, 2)
        randcy = random.randint(1, 2)
        randjp = random.randint(1, 27)

        # Red Rectangle
        redrectstats = redrectx, redrecty, redrectw, redrectl
        redrect = pygame.draw.rect(window, (255, 0, 0), redrectstats)

        # Blue Rectangle
        bluerectstats = bluerectx, bluerecty, bluerectw, bluerectl
        bluerect = pygame.draw.rect(window, (0, 0, 255), bluerectstats)

        # Circle
        circlecenter = circlex, circley
        circle = pygame.draw.circle(window, (255, 255, 255), circlecenter, circler)

        # Collision stats
        redcx = redrectx + 25
        redcy = redrecty + 25
        bluecx = bluerectx + 25
        bluecy = bluerecty + 25
        reddx = abs(redcx - circlex)
        reddy = abs(redcy - circley)
        bluedx = abs(bluecx - circlex)
        bluedy = abs(bluecy - circley)

        # Movements
        if redrectx > 0:
            if keys[pygame.K_a]:
                redrectx -= rectanglev

        if redrectx < 750:
            if keys[pygame.K_d]:
                redrectx += rectanglev

        if redrecty > 0:
            if keys[pygame.K_w]:
                redrecty -= rectanglev

        if redrecty < 550:
            if keys[pygame.K_s]:
                redrecty += rectanglev

        if bluerectx > 0:
            if keys[pygame.K_LEFT]:
                bluerectx -= rectanglev

        if bluerectx < 750:
            if keys[pygame.K_RIGHT]:
                bluerectx += rectanglev

        if bluerecty > 0:
            if keys[pygame.K_UP]:
                bluerecty -= rectanglev

        if bluerecty < 550:
            if keys[pygame.K_DOWN]:
                bluerecty += rectanglev

        # Moving the circle to random coordinates
        if randcx == 1 and circlex + randvx < 775:
            circlex += randvx
        elif randcx == 2 and circlex - randvx > 0:
            circlex -= randvx
        if randcy == 1 and circley + randvy < 575:
            circley += randvy
        elif randcy == 2 and circley - randvy > 0:
            circley -= randvy

        if randjp == 27:
            circlex = random.randint(25, 775)
            circley = random.randint(25, 575)

        # Collision
        if reddx <= 50 and reddy <= 50:
            bluewins()
        if bluedx <= 50 and bluedy <= 50:
            redwins()

    if winner == 'red' and game_ended:
        redwins()

    if winner == 'blue' and game_ended:
        bluewins()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

