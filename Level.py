import pygame
from Block import *
from consts import *

class Level:

    def __init__(self, level):
        self.x = 0
        self.y = 0
        self.rows = level.split()
        self.buildLevel()

    # Builds and draws the grid
    def buildLevel(self):
        self.levelMap = []
        self.image = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        myRect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        for i in range(GRID_HEIGHT):
            blocks = []
            for j in range(GRID_WIDTH):
                if self.rows[i][j] == '*':
                    # Append new block
                    blocks.append(Block(pygame.Rect(myRect), BLUE, True, (i, j)))
                    # Draw to surface
                    pygame.draw.rect(self.image, BLUE, myRect)
                else:
                    blocks.append(Block(pygame.Rect(myRect), WHITE, False, (i, j)))
                myRect.left += BLOCK_SIZE
            self.levelMap.append(blocks)
            myRect.left = 0
            myRect.top += BLOCK_SIZE
