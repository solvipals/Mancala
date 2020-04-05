# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:49:33 2020

@author: SOPA
"""
from Board import print_state

def finish_game(state):
    count = 0
    if sum(state[0:6]) == 0:
        for i in range(7, 13):
            count = count + state[i]
            state[i] = 0

        state[13] = state[13] + count
        print_state(state)
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        print('%                                 %')
        print('%%%%%%%%%%%  GAME OVER %%%%%%%%%%%%')
        print('%                                 %')
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        return True
    if sum(state[7:13]) == 0:
        for i in range(6):
            count = count + state[i]
            state[i] = 0

        state[6] = state[6] + count

        print_state(state)
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        print('%                                 %')
        print('%%%%%%%%%%%  GAME OVER %%%%%%%%%%%%')
        print('%                                 %')
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        return True
    return False