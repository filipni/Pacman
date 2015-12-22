from consts import *
from Ghost import *

class Inky(Ghost):

    def __init__(self, pos):
        super().__init__('Inky', LIGHT_BLUE, pos)

    def Update(self, entities, grid):
        assert 'Pac' in entities and 'Blinky' in entities, 'Pacman and Blinky must be in the dictionary'
        pac = entities['Pac'].pos
        blinky = entities['Blinky'].pos


