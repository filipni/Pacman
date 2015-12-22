#! /usr/bin/python3
import pygame, sys, logging
from pygame.locals import *
from consts import *
from MovingObject import *
from Level import *
from Ghost import *
from Blinky import *

def handleInput(event, pac):
    pac.prevDir = pac.direction
    if event.key == pygame.K_UP:
        pac.direction = UP
    elif event.key == pygame.K_DOWN:
        pac.direction = DOWN
    elif event.key == pygame.K_LEFT:
        pac.direction = LEFT
    elif event.key == pygame.K_RIGHT:
        pac.direction = RIGHT

# Enable logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

# Initialization
pygame.init()
DISPSURF = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
FPSCLOCK = pygame.time.Clock()

# Load the level
levelFile = open('level1.txt')
levelData = levelFile.read()
level = Level(levelData)

# Create pacman and the ghosts
pac = MovingObject(YELLOW, (1, 3))
blinky = Blinky((11, 13))

entities = [pac, blinky]

#The game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            handleInput(event, pac)

    pac.Move(level.levelMap)
    blinky.chooseDest(pac.pos, level.levelMap)
    blinky.Move(level.levelMap)

    # Draw
    DISPSURF.blit(level.image, (0,0))
    for ent in entities:
        pygame.draw.rect(DISPSURF, ent.color, ent.rect)

    # Update display
    pygame.display.update()
    FPSCLOCK.tick(FPS)

    # End the game if any of the ghosts have caught pacman
    if pac.rect.colliderect(blinky.rect):
        print('Game Over!')
        break

logging.debug('End of program')
