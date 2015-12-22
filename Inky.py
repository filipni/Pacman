from consts import *
from Ghost import *

class Inky(Ghost):

    def __init__(self, pos):
        super().__init__(LIGHT_BLUE, pos)

    def chooseDest(self, pacsPos, grid):
        pass

