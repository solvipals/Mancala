# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 13:19:37 2020

@author: andri
"""

from Board import *

def twoplayer():
    state = initialize_game()
    
    while (not finish_game(state)):
        print_state(state)
    
        validInput = False
        while not validInput:
            if state[14]==1:
                print("Player 1's turn")
            elif state[14]==-1:
                print("Player 2's turn")
            
            choice = input("Choose a pocket :    ")
            try:
                choice = int(choice)
                try:
                    if choice in getoptions(state):
                        validInput = True
                        print(" ")
                        print("Choice was valid. Pebbles from pocket {} were moved".format(choice))
                        print(" ")
                    else:
                        raise Exception
                except Exception as e:
                    print("The pocket you chose is invalid. It is not yours or it is empty.")
                    print("Check the board and try again")
                    print("  ")
            except ValueError:
                print("Only integers are allowed, please try again")
                
        
        
        move(state, choice)
        
    print_state(state)