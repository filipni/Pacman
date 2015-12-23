#! /usr/bin/python3
import pygame, sys, logging
from pygame.locals import *
from consts import *
from MovingObject import *
from Level import *
from Ghost import *
from Blinky import *
from Pinky import *
from Inky import *
from Clyde import *

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
#blinky = Blinky((11, 13))
#pinky = Pinky((11, 13))
#inky = Inky((11,13))
clyde = Clyde((11,13))

entities = {'Pac': pac, clyde.name: clyde} #, blinky.name: blinky, inky.name: inky, pinky.name: pinky}
ghosts = [clyde] #, blinky, inky, pinky] # Don't forget to add ghosts to this list AND entities above!
#blinky.scatter, inky.scatter, pinky.scatter, clyde.scatter = True, True, True, True

#The game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            logging.debug('End of program')
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            handleInput(event, pac)

    pac.Move(level.levelMap)

    for ghost in ghosts:
        ghost.Update(entities, level.levelMap)
        ghost.Move(level.levelMap)

    # Draw
    DISPSURF.blit(level.image, (0,0))
    for ent in entities.values():
        pygame.draw.rect(DISPSURF, ent.color, ent.rect)

    # Update display
    pygame.display.update()
    FPSCLOCK.tick(FPS)

    # End the game if any of the ghosts have caught pacman
    for ghost in ghosts:
        if ghost.rect.colliderect(pac.rect):
            print('Game Over!')
            logging.debug('End of program')
            sys.exit()

