# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 19:44:14 2020

@author: andri
"""
import os
from Game_Operations import *
from Board import *
from minimax import *
import copy
import time

state = initialize_game()

depth=0
while depth<=0 or depth>15:
    print("Choose difficulty level from 1-20")
    depth=int(input())
    if depth<=0 or depth>15:
        print("Invalid input")
        


while (not finish_game(state)):
    print_state(state)
    
    if state[14]==1:
        print("Player 1's turn")
        start = time.time()
        best_score,best_move = maxi(state,depth-4, -49, 49)
        end = time.time()
        print('Evaluation time: {}s'.format(round(end - start, 7)))
        print('Recommended move: {}'.format(best_move))
        print("Score with the reccommended move: {}".format(best_score))
        
        print("Choose your master")
        choice = int(input())

        if move(state, choice) == []:
            print("This move is not valid. Please choose another one")
        else:
            move(state, choice)

    elif state[14]==-1:
        best_score,best_move = mini(state,depth, -49, 49)
        #print(best_score , best_move)
        move(state,best_move)
        #print("Player2's turn") 
    
print_state(state)