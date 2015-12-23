from consts import *
from MovingObject import *

class Pacman(MovingObject):
    def __init__(self):
        super().__init__(YELLOW, PAC_START)
        self.name = 'Pac'

    def Update(self, event, entities, grid):
        if event != None and event.type == pygame.KEYDOWN:
                self.prevDir = self.direction
                if event.key == pygame.K_UP:
                        self.direction = UP
                elif event.key == pygame.K_DOWN:
                        self.direction = DOWN
                elif event.key == pygame.K_LEFT:
                        self.direction = LEFT
                elif event.key == pygame.K_RIGHT:
                        self.direction = RIGHT

