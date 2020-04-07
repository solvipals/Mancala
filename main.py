# -*- coding: utf-8 -*-



#Eftir ad skrifa main 

import os 
from Board import *
from Game_Operations import *
from minimax import *
state = initialize_game()


while (True):
    print_state(state)
    result = finish_game(state)
    
    if (result != None):
        print("Score is {}".format(result))
    
    c = True
    if state[14]==1:
        print("Player 1's turn")
        while(c):
            print("Choose your master")
            choice = int(input())
            o  = getoptions(state)
            if (choice in o):
                move(state, choice)
                c = False
            else:
                print("Invalid Move you piece of shit, choose something valid")
        
    elif state[14]==-1:
        state1 = copy.deepcopy(state)
        (m, choice) = maxi(state)
        state = state1
        move(state, choice)
    


print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print('%                                 %')
print('%%%%%%%%%%%  GAME OVER %%%%%%%%%%%%')
print('%                                 %')
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%') 