
import os
from Board import *
from Algorithms.abminimax import *
import copy
import time

def zeroplayer():
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
    
    validInput = False
    while not validInput:
        print("Choose seconds between moves so you can better inspect what the computer does.")
        print("This number can be between 0.0 and 3.0 seconds.")
        print("0.0 will be pretty fast, depending on the chosen depth.")
        print("3.0 will be pretty slow, depending on the chosen depth.")
        print(" ")
        timesleep=input("Choose time between moves :    ")
        try:
            timesleep = float(timesleep)
            try:
               if (timesleep>=0.0 and timesleep<=3.0):
                   validInput = True
               else:
                   raise Exception 
            except Exception:
                print("Invalid Choice. Difficulty level must be between 0 and 12")
                
        except ValueError:
            print("Only floats are allowed")
    
            
            
    while (not finish_game(state)):
        print_state(state)
        time.sleep(timesleep)
        if state[14]==1:
            
            cprint("Player 1 is thinking...", "white", "on_magenta")
            print(" ")
            start = time.time()
            best_score,best_move = maxi(state,depth1, -49, 49)
            end = time.time()
            
            print("Chosen depth for Player 1 was : {}".format(depth1))
            print('Evaluation time : {} seconds'.format(round(end - start, 7)))
            print('Best move for Player 1: {}'.format(best_move))
            print("Expected score after {} moves is: {}".format(depth1, best_score))
            
            
            
            #print(best_score , best_move)
            move(state,best_move)
    
        elif state[14]==-1:
            
            print("Player 2 is thinking...")
            print(" ")
            start = time.time()
            best_score,best_move = mini(state,depth2, -49, 49)
            end = time.time()
            
            print("Chosen depth for Player 2 was : {}".format(depth2))
            print('Evaluation time : {} seconds'.format(round(end - start, 7)))
            print('Best move for Player 1: {}'.format(best_move))
            print("Expected score after {} moves is: {}".format(depth1, best_score))

            #print(best_score , best_move)
            move(state,best_move)
            #print("Player2's turn") 
        
    print_state(state)