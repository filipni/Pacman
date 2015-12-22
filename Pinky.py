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
            if y < 0:
                y = 0
            x -= 4
            if x < 0:
                x = 0
        elif pac.direction == DOWN:
            y += 4
            if y > GRID_HEIGHT - 1:
                y = GRID_HEIGHT - 1
        elif pac.direction == LEFT:
            x -= 4
            if x < 0:
                x = 0
        else:
            x += 4
            if x > GRID_WIDTH - 1:
                x = GRID_WIDTH -1

        super().chooseDest((y,x), grid)
