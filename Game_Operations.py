# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:49:33 2020

@author: SOPA
"""

def finish_game(state):
    count = 0
    if sum(state[0:6]) == 0:
        for i in range(7, 13):
            count = count + state[i]
            state[i] = 0

        state[13] = state[13] + count
        
        result = state[13]-state[6]
        
        return result
           
        
    elif sum(state[7:13]) == 0:
        for i in range(6):
            count = count + state[i]
            state[i] = 0

        state[6] = state[6] + count

        result = state[13]-state[6]
        
        return result
    
    
    else:
        return None