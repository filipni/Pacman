from consts import *
from Ghost import *

class Inky(Ghost):

    def __init__(self, pos):
        super().__init__('Inky', LIGHT_BLUE, pos)

    def Update(self, entities, grid):
        assert 'Pac' in entities and 'Blinky' in entities, 'Pacman and Blinky must be in the dictionary'
        pac = entities['Pac']
        blinky = entities['Blinky']

        y = pac.pos[0]
        x = pac.pos[1] + 2

        diffY = y-blinky.pos[0]
        diffX = x-blinky.pos[1]

        y = blinky.pos[0] + diffY * 2
        x = blinky.pos[1] + diffX * 2

        super().chooseDest(self.CheckPosBounds((y, x)), grid)

