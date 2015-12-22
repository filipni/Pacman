from consts import *
from Ghost import *
import logging

class Blinky(Ghost):

    def __init__(self, pos):
        super().__init__('Blinky', RED, pos)

    def Update(self, entities, grid):
        assert 'Pac' in entities, 'Pacman must be in the dictionary' 
        super().chooseDest(entities['Pac'].pos, grid)

