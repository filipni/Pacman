from consts import *
from Ghost import *

class Inky(Ghost):

    def __init__(self, pos):
        super().__init__('Inky', LIGHT_BLUE, pos, (31, 27))

    def ChaseUpdate(self, entities):
        assert 'Pac' in entities and 'Blinky' in entities, 'Pacman and Blinky must be in the dictionary'
        pac = entities['Pac']
        blinky = entities['Blinky']

        y = pac.pos[0]
        x = pac.pos[1] + 2

        diffY = y-blinky.pos[0]
        diffX = x-blinky.pos[1]

        y = blinky.pos[0] + diffY * 2
        x = blinky.pos[1] + diffX * 2

        return self.CheckPosBounds((y, x))

