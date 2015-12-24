import math
from consts import *
from MovingObject import *
from abc import ABCMeta, abstractmethod

class Ghost(MovingObject):

    __metaclass__ = ABCMeta

    def __init__(self, name, color, pos, homePos):
        super().__init__(color, pos)
        self.name = name
        self.homePos = homePos
        self.scatter = False
        self.dest = (0, 0)

    def chooseDest(self, grid):
        options = self.directionAlts(grid) # options is a list of tuples containing a block and its direction
        bestBlock =  None
        bestDir = None
        minDist = 9999 # Initial value represents infinity

        # Find the best way based on the distance in a straightline from each option to pacman
        for direction, block in options.items():
            dist = self.calcDist(self.dest, block.pos)
            if bestBlock == None or dist < minDist:
                minDist = dist
                bestBlock = block
                bestDir = direction

        # The ghost can only turn if it's aligned correctly
        if self.alignedV(self.rect, bestBlock.rect) and (bestDir == UP or bestDir == DOWN):
            self.direction = bestDir

        elif self.alignedH(self.rect, bestBlock.rect) and (bestDir == LEFT or bestDir == RIGHT):
            self.direction = bestDir

    def calcDist(self, pos1, pos2):
        return math.hypot(pos1[1]-pos2[1], pos1[0]-pos2[0])

    def directionAlts(self, grid):
        dirs = {}
        y, x = self.pos[0], self.pos[1]

        if not grid[y+1][x].solid and self.direction != UP:
            dirs[DOWN] = grid[y+1][x]
        if not grid[y-1][x].solid and self.direction != DOWN:
            dirs[UP] = grid[y-1][x]
        if not grid[y][x+1].solid and self.direction != LEFT:
            dirs[RIGHT] = grid[y][x+1]
        if not grid[y][x-1].solid and self.direction != RIGHT:
            dirs[LEFT] = grid[y][x-1]

        # Some blocks doesn't allow the ghosts to turn upwards
        if grid[y][x].noUp:
            dirs.pop(UP, None)

        return dirs

    def Update(self, event, entities, grid):
        block = grid[ self.pos[0] ][ self.pos[1] ]
        if block.cross:
            if self.scatter:
                self.dest = self.homePos
            else:
                self.ChaseUpdate(entities)
        self.chooseDest(grid)

    @abstractmethod
    def ChaseUpdate(self, entities):
        pass
