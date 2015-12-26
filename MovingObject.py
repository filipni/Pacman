import pygame
from consts import *
from Block import *
from abc import ABCMeta, abstractmethod

class MovingObject():
    def __init__(self,color,pos):
        self.speed = PAC_SPEED
        self.direction = DOWN
        self.prevDir =  DOWN
        self.pos = pos
        self.color = color
        self.calcRect()
        self.prevBlock = None

    @abstractmethod
    def Update(self, event, entities, grid):
        pass

    # Wrapping for the real move method to improve the steering
    def Move(self, grid):
        if self.__Move(self.direction, grid):
            self.prevDir = None
        else:
            self.__Move(self.prevDir, grid)
        self.CheckBounds()

    def CheckBounds(self):
        if self.pos[1] < 1:
            self.pos = (self.pos[0], GRID_WIDTH - 2)
            self.calcRect()
        elif self.pos[1] > GRID_WIDTH - 2:
            self.pos = (self.pos[0], 1)
            self.calcRect()
        elif self.pos[0] < 1:
            self.pos = (GRID_HEIGHT - 2, self.pos[1])
            self.calcRect()
        elif self.pos[0] > GRID_HEIGHT - 2:
            self.pos = (1, self.pos[1])
            self.calcRect()

    def CheckPosBounds(self, pos):
        y = pos[0]
        x = pos[1]

        if y > GRID_HEIGHT - 1:
            y = GRID_HEIGHT - 1
        elif y < 0:
            y = 0

        if x > GRID_WIDTH - 1:
            y = GRID_WIDTH - 1
        elif x < 0:
            x = 0

        return (y, x)

    def calcRect(self):
        self.rect = self.rect = pygame.Rect(self.pos[1] * BLOCK_SIZE, self.pos[0] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)

    def __Move(self, direction, grid):
        if direction == UP:
            nextBlock =  grid[ self.pos[0] - 1 ][ self.pos[1] ]
            self.rect.y -= self.speed
            if nextBlock.rect.colliderect(self.rect):
                if nextBlock.solid or not self.alignedV(self.rect, nextBlock.rect):
                    self.rect.top = nextBlock.rect.bottom
                    return False
            if self.rect.y < nextBlock.rect.y + BLOCK_SIZE / 2:
                self.prevPos = self.pos
                self.pos = (self.pos[0] - 1, self.pos[1])

        elif direction == DOWN:
            nextBlock = grid[ self.pos[0] + 1 ][ self.pos[1] ]
            self.rect.y += self.speed
            if nextBlock.rect.colliderect(self.rect):
                if nextBlock.solid or not self.alignedV(self.rect, nextBlock.rect):
                    self.rect.bottom = nextBlock.rect.top
                    return False
            if self.rect.bottom > (nextBlock.rect.top + BLOCK_SIZE / 2):
                self.prevPos = self.pos
                self.pos = (self.pos[0] + 1, self.pos[1])

        elif direction == LEFT:
            nextBlock = grid[ self.pos[0]][ self.pos[1] - 1 ]
            self.rect.x -= self.speed
            if nextBlock.rect.colliderect(self.rect):
                if nextBlock.solid or not self.alignedH(self.rect, nextBlock.rect):
                    self.rect.left = nextBlock.rect.right
                    return False
            if self.rect.left < (nextBlock.rect.x + BLOCK_SIZE / 2):
                self.prevPos = self.pos
                self.pos = self.pos[0], self.pos[1] - 1

        elif direction == RIGHT:
            nextBlock = grid[ self.pos[0] ][ self.pos[1] + 1 ]
            self.rect.x += self.speed
            if nextBlock.rect.colliderect(self.rect):
                if nextBlock.solid or not self.alignedH(self.rect, nextBlock.rect):
                    self.rect.right = nextBlock.rect.left
                    return False
            if self.rect.right > nextBlock.rect.x + BLOCK_SIZE / 2:
                self.prevPos = self.pos
                self.pos = (self.pos[0], self.pos[1] + 1)
        else:
            return False
        return True

    def printPos(self):
        print("x: " + str(self.pos[1]) + ", y: " + str(self.pos[0]))

    def alignedV(self, rect1, rect2):
        return rect1.x == rect2.x

    def alignedH(self, rect1, rect2):
        return rect1.y == rect2.y


