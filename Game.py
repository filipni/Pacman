#! /usr/bin/python3
import pygame, sys, logging
from pygame.locals import *
from consts import *
from MovingObject import MovingObject
from Level import Level
from Ghost import Ghost
from Blinky import Blinky
from Pinky import Pinky
from Inky import Inky
from Clyde import Clyde
from Pacman import Pacman

class Game():
    def __init__(self):

        # Initialization
        pygame.init()
        self.DISPSURF = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        self.FPSCLOCK = pygame.time.Clock()

        # Load the level
        levelFile = open('level1.txt')
        levelData = levelFile.read()
        self.level = Level(levelData)

        # Create pacman and the ghosts
        self.pac = Pacman()
        blinky = Blinky()
        pinky = Pinky()
        inky = Inky()
        clyde = Clyde()

        self.entities = {self.pac.name: self.pac, blinky.name: blinky, clyde.name: clyde, inky.name: inky, pinky.name: pinky}

        # Scatter timer
        pygame.time.set_timer(USEREVENT+1, 5000)

        self.quit = False

    def Update(self):

        # End the game if any of the ghosts have caught pacman
        for ent in self.entities.values():
            if ent.name != 'Pac' and ent.rect.colliderect(self.pac.rect):
                print('Game Over!')
                print('Killed by: ' + ent.name)
                print('Time survived: ' + str(pygame.time.get_ticks()/1000) + ' seconds')
                self.quit = True

        # Handle events
        keydownEvent = None
        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit = True
            if event.type == pygame.KEYDOWN:
                keydownEvent = event
            if event.type == USEREVENT+1:
                self.toggleScatter()

        # Update and move all entities
        for ent in self.entities.values():
            ent.Update(keydownEvent, self.entities, self.level.levelMap)
            ent.Move(self.level.levelMap)

    # Used to swtich ghosts from chase to scatter mode and vice versa
    def toggleScatter(self):
        for ent in self.entities.values():
            if ent.name != 'Pac':
                ent.scatter = not ent.scatter


    def Draw(self):
        # Draw
        self.DISPSURF.blit(self.level.image, (0,0))
        for ent in self.entities.values():
            pygame.draw.rect(self.DISPSURF, ent.color, ent.rect)

        # Update display
        pygame.display.update()
        self.FPSCLOCK.tick(FPS) # Gives us the right FPS

