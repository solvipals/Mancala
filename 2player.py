# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 13:19:37 2020

@author: andri
"""

from Board import *
from Game_Operations import *

state = initialize_game()


while (not finish_game(state)):
    print_state(state)
    
    if state[14]==1:
        print("Player 1's turn")
    elif state[14]==-1:
        print("Player2's turn")
        
    print("Choose your master")
    choice = int(input())
    
    if move(state, choice) == []:
        print("This move is not valid. Please choose another one")
    else:
        move(state, choice)
    
print_state(state)