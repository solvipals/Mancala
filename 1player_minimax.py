# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 19:44:14 2020

@author: andri
"""

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
        best_score,best_move = mini(state,depth)
        #print(best_score , best_move)
        move(state,best_move)
        #print("Player2's turn") 
    
print_state(state)