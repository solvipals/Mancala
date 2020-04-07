# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 13:32:07 2020

@author: andri
"""

# Eftir ad skrifa main 

from Board import *
from Game_Operations import *
from tree_generator import *

state = initialize_game()

depth=0
while depth<=0 or depth>8:
    print("Choose difficulty level from 1-8")
    depth=int(input())
    if depth<=0 or depth>8:
        print("Invalid input")
        


while (not finish_game(state)):
    print_state(state)
    
    if state[14]==1:
        print("Player 1's turn")

        print("Choose your master")
        choice = int(input())

        if move(state, choice) == []:
            print("This move is not valid. Please choose another one")
        else:
            move(state, choice)

    elif state[14]==-1:
        state_tree=tree_state_generator(state,depth)
        score_tree=score_tree_generator(state_tree,depth)
        #print(state_tree)
        print(score_tree[0])
        best_move=int(score_tree[0].index(np.nanmin(score_tree[0])))
        move(state,best_move+7)
        #print("Player2's turn") 
    
print_state(state)