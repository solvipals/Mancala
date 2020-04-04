# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:49:33 2020

@author: SOPA
"""

   
def finish_game(state):
    count = 0
    if (sum(state[0:6]) == 0):
        for i in range (7, 13):
            count = count+state[i]
        
        state[13] = state[13]+count
        return True
    
    elif (sum(state[7:12]) == 0):
        for i in range (6):
            count = count+state[i]
        state[6] = state[6]+count
        return True
    else:
        return False
    
    
    