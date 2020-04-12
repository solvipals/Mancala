# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 13:19:37 2020

@author: andri
"""

from Board import *
from termcolor import colored, cprint


def twoplayer():
    state = initialize_game()
    
    while (not finish_game(state)):
        print_state(state)
    
        validInput = False
        while not validInput:
            if state[14]==1:
                cprint("Player 1's turn", "grey", "on_white")
            elif state[14]==-1:
                cprint("Player 2's turn" , "grey", "on_white")
            
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
        
    print_state(state)