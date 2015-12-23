from consts import *
from Ghost import *

class Clyde(Ghost):

    def __init__(self, pos):
        super().__init__('Clyde', ORANGE, pos, (31, 0))

    def ChaseUpdate(self, entities):
        pac = entities['Pac']
        distToPac = self.calcDist(self.pos, pac.pos)
        if distToPac > 8:
            return pac.pos
        else:
            return self.homePos
