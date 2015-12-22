import math
from consts import *
from MovingObject import *
from abc import ABCMeta, abstractmethod

class Ghost(MovingObject):

    __metaclass__ = ABCMeta

    def __init__(self, name, color, pos):
        super().__init__(color, pos)
        self.name = name
        destination = None

    def chooseDest(self, destPos, grid):
        options = self.directionAlts(grid) # options is a list of tuples containing a block and its direction
        bestWay =  None
        minDist = 9999 # Initial value represents infinity

        # Find the best way based on the distance in a straightline from each option to pacman
        for way in options:
            dist = self.calcDist(destPos, way[0].pos)
            if bestWay == None or dist < minDist:
                minDist = dist
                bestWay = way

        # The ghost can only turn if it's aligned correctly
        if self.alignedV(self.rect, bestWay[0].rect) and (bestWay[1] == UP or bestWay[1] == DOWN):
            self.direction = bestWay[1]

        elif self.alignedH(self.rect, bestWay[0].rect) and (bestWay[1] == LEFT or bestWay[1] == RIGHT):
            self.direction = bestWay[1]

    def calcDist(self, pos1, pos2):
        return math.hypot(pos1[1]-pos2[1], pos1[0]-pos2[0])

    def directionAlts(self, grid):
        dirs = []
        y, x = self.pos[0], self.pos[1]
        if not grid[y+1][x].solid and self.direction != UP:
            dirs.append((grid[y+1][x], DOWN))
        if not grid[y-1][x].solid and self.direction != DOWN:
            dirs.append((grid[y-1][x], UP))
        if not grid[y][x+1].solid and self.direction != LEFT:
            dirs.append((grid[y][x+1], RIGHT))
        if not grid[y][x-1].solid and self.direction != RIGHT:
            dirs.append((grid[y][x-1], LEFT))
        return dirs

    @abstractmethod
    def Update(self, entities, grid):
        pass

