import pygame
from Block import *
from consts import *

class Level:

    def __init__(self, level):
        self.x = 0
        self.y = 0
        self.rows = level.split()
        self.buildLevel()
        self.image = pygame.image.load('level1.png')
        self.image = pygame.transform.scale(self.image, (WINDOW_WIDTH, WINDOW_HEIGHT))

    # Builds and draws the grid
    def buildLevel(self):
        self.levelMap = []
        myRect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        for i in range(GRID_HEIGHT):
            blocks = []
            for j in range(GRID_WIDTH):
                if self.rows[i][j] == '*':
                    # Append new block
                    blocks.append(Block(pygame.Rect(myRect), BLUE, True, False, False,  (i, j)))
                elif self.rows[i][j] == 'c':
                    blocks.append(Block(pygame.Rect(myRect), WHITE, False, True, False,  (i, j)))
                elif self.rows[i][j] == 'u':
                    blocks.append(Block(pygame.Rect(myRect), WHITE, False, True, True, (i, j)))
                else:
                    blocks.append(Block(pygame.Rect(myRect), WHITE, False, False, False, (i, j)))
                myRect.left += BLOCK_SIZE
            self.levelMap.append(blocks)
            myRect.left = 0
            myRect.top += BLOCK_SIZE
