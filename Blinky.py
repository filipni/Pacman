from consts import *
from Ghost import *
import logging

class Blinky(Ghost):

    def __init__(self):
        super().__init__('Blinky', RED, GHOST_START, BLINKY_HOME)

    def ChaseUpdate(self, entities):
        assert 'Pac' in entities, 'Pacman must be in the dictionary' 
        return entities['Pac'].pos

