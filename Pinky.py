from consts import *
from Ghost import *

class Pinky(Ghost):

    def __init__(self, pos):
        super().__init__(PINK, pos)

    def chooseDest(self, pacsPos, grid):
        pass

