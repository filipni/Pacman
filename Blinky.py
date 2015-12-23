from consts import *
from Ghost import *
import logging

class Blinky(Ghost):

    def __init__(self, pos):
        super().__init__('Blinky', RED, pos, (0, 26))

    def ChaseUpdate(self, entities):
        assert 'Pac' in entities, 'Pacman must be in the dictionary' 
        return entities['Pac'].pos

