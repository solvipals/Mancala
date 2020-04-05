# -*- coding: utf-8 -*-



#Eftir ad skrifa main 

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
    
    state = move(state, choice)
    
