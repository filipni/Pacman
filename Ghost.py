import math
from consts import *
from MovingObject import *
from abc import ABCMeta, abstractmethod

class Ghost(MovingObject):

    __metaclass__ = ABCMeta

    def __init__(self, color, pos):
        super().__init__(color, pos)
        destination = None

    @abstractmethod
    def chooseDest(self, pacsPos, grid):
        pass

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

