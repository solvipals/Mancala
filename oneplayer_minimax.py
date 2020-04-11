# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 19:44:14 2020

@author: andri
"""
import os
from Board import *
from abminimax import *
import copy
import time
from termcolor import colored, cprint

def oneplayer():
    state = initialize_game()
    
    ##########################Choose difficulty level##################################
    validInput = False
    while not validInput:
        depth=input("Choose difficulty level for the computer from 1-12 :    ")
        try:
           depth = int(depth)
           try:
               if (depth>=0 and depth<=12):
                   validInput = True
               else:
                   raise Exception 
           except Exception:
                print("Invalid Choice. Difficulty level must be between 0 and 12.")
                
        except ValueError:
            print("Only integers are allowed, please choose again!")
            
    
    ##########################Does the player want help??################################
    
    validInput = False
    while not validInput:
        print("Would you like the computer to reccommend the best move for you?")
        wanthelp = input("1 = YES         0 = NO:         ")
        try:
           wanthelp = int(wanthelp)
           try:
               if (wanthelp == 1 or wanthelp == 0):
                   validInput = True
               else:
                   raise Exception 
           except Exception:
                print("Invalid Choice. Input can only be 0 or 1")
                
        except ValueError:
            print("Only integers are allowed, please choose again!")
    
    
    ###########################Run the game##############################################
    
    while (not finish_game(state)):
        print_state(state)
        
        
        
        if state[14]==1:
            print("Player 1's turn")
            if (state[6] - state[13] < -7 and wanthelp == 0):
                print("Are you sure you dont want any help? You are being dominated...")
                
                validInput = False
                while not validInput:
                    print("Would you like the computer to reccommend the best move for you?")
                    wanthelp = input("1 = YES         0 = NO:         ")
                    try:
                       wanthelp = int(wanthelp)
                       try:
                           if (wanthelp == 1 or wanthelp == 0):
                               validInput = True
                           else:
                               raise Exception 
                       except Exception:
                            print("Invalid Choice. Input can only be 0 or 1")
                            
                    except ValueError:
                        print("Only integers are allowed, please choose again!")
                
            if (wanthelp == 1):
                start = time.time()
                best_score,best_move = maxi(state,depth, -49, 49)
                end = time.time()
                print('Evaluation time : {}s'.format(round(end - start, 7)))
                print('Recommended move for Player 1 : {}'.format(best_move))
                print("Expected score after {} moves is: {}".format(depth, best_score))
            
            
            validInput = False
            while not validInput:
                
                choice = input("Choose a pocket :    ")
                try:
                    choice = int(choice)
                    try:
                        if choice in getoptions(state):
                            validInput = True
                            print(" ")
                            cprint("Choice was valid. Pebbles from pocket {} were moved".format(choice), "white", "on_green")
                            print(" ")
                        else:
                            raise Exception
                    except Exception as e:
                        cprint("The pocket you chose is invalid. It is not yours or it is empty.", "white", "on_red")
                        cprint("Check the board and try again",  "white", "on_red")
                        print("  ")
                        
                except ValueError:
                    cprint("Only integers are allowed, please try again", "white", "on_red")
                
            move(state, choice)
    
        elif state[14]==-1:
            best_score,best_move = mini(state,depth, -49, 49)
            #print(best_score , best_move)
            move(state,best_move)
            #print("Player2's turn") 
        
    print_state(state)