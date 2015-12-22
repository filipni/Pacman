from consts import *
from Ghost import *

class Pinky(Ghost):

    def __init__(self, pos):
        super().__init__('Pinky', PINK, pos)

    def Update(self, entities, grid):
        assert 'Pac' in entities, 'Pacman must be in the dictionary'

        pac = entities['Pac']
        y = pac.pos[0]
        x = pac.pos[1]

        if pac.direction == UP:
            y -= 4
            x -= 4
        elif pac.direction == DOWN:
            y += 4
        elif pac.direction == LEFT:
            x -= 4
        else:
            x += 4

        super().chooseDest(self.CheckPosBounds((y,x)), grid)
