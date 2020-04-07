# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 11:13:46 2020

@author: SOPA
"""
import copy
from Board import *
from Game_Operations import *

def mini(state):
    
    minv = 48
    xi = None

    result = finish_game(state)
    
    if (result != None):
        return (minv, xi)

        
        
    statecopy = copy.deepcopy(state)
    turn = statecopy[14]
    
    for i in getoptions(state):
        state2 = move(state, i)
        
        if(turn == state2[14]):
            (m, min_i) = mini(state2)
        else: 
            (m, max_i) = maxi(state2)
        
        if m < minv:
            minv = m
            xi = i

        state = statecopy
        
    return (minv, xi)


def maxi(state):
    
    maxv = -48
    xi = None
    
    
    result = finish_game(state)
    
    if (result != None):
        return (maxv, xi)
            
    
    statecopy = copy.deepcopy(state)
    turn = statecopy[14]
    
    for i in getoptions(state):

        state2 = move(state, i)
        
        if(turn == state2[14]):
            (m, max_i) = maxi(state2)
        else: 
            (m, min_i) = mini(state2)
        
        if m > maxv:
            maxv = m
            xi = i

        state = statecopy
        
    return (maxv, xi)
            
