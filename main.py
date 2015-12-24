#! /usr/bin/python3
import sys, logging
from Game import Game

# Enable logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

game = Game()

#The game loop
while not game.quit:
    game.Update()
    game.Draw()

game.Quit()
logging.debug('End of program')

