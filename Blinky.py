from consts import *
from Ghost import *
import logging

class Blinky(Ghost):

    def __init__(self, pos):
        super().__init__(RED, pos)

    def chooseDest(self, pacsPos, grid):
        options = self.directionAlts(grid) # options is a list of tuples containing a block and its direction
        bestWay =  None
        minDist = 9999 # Initial value represents infinity

        # Find the best way based on the distance in a straightline from each option to pacman
        for way in options:
            dist = self.calcDist(pacsPos, way[0].pos)
            if bestWay == None or dist < minDist:
                minDist = dist
                bestWay = way

        # The ghost can only turn if it's aligned correctly
        if self.alignedV(self.rect, bestWay[0].rect) and (bestWay[1] == UP or bestWay[1] == DOWN):
            self.direction = bestWay[1]

        elif self.alignedH(self.rect, bestWay[0].rect) and (bestWay[1] == LEFT or bestWay[1] == RIGHT):
            self.direction = bestWay[1]

