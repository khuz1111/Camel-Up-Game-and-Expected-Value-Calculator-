from Game_board import Game_board
from Game_Manager import Game_Manager
import time
import random
from inputimeout import inputimeout
from copy import deepcopy


players = ['Henry', 'Muhammad']
GM = Game_Manager(players)
GM.setup_game()
GM.play_game()



