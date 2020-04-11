
import os
from Board import *
from abminimax import *
import copy
import time

state = initialize_game()

validInput = False
while not validInput:
    depth1=input("Choose difficulty level for player 1 from 1-12 :    ")
    try:
       depth1 = int(depth1)
       try:
           if (depth1>=0 and depth1<=12):
               validInput = True
           else:
               raise Exception 
       except Exception:
            print("Invalid Choice. Difficulty level must be between 0 and 12")
            
    except ValueError:
        print("Only integers are allowed")
    
   
    
validInput = False
while not validInput:
    depth2=input("Choose difficulty level for Player 2 from 1-12 :    ")
    try:
       depth2 = int(depth2)
       try:
           if (depth2>=0 and depth2<=12):
               validInput = True
           else:
               raise Exception 
       except Exception:
            print("Invalid Choice. Difficulty level must be between 0 and 12")
            
    except ValueError:
        print("Only integers are allowed")
        
        
while (not finish_game(state)):
    print_state(state)
    time.sleep(1)
    if state[14]==1:
        best_score,best_move = maxi(state,depth1, -49, 49)
        #print(best_score , best_move)
        move(state,best_move)

    elif state[14]==-1:
        best_score,best_move = mini(state,depth2, -49, 49)
        #print(best_score , best_move)
        move(state,best_move)
        #print("Player2's turn") 
    
print_state(state)