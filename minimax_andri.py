# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 18:41:44 2020

@author: andri
"""


from Board import *
from Game_Operations import *


def mini(state,depth):
    depth-=1
    current_state=copy.deepcopy(state)
    miniv=49
    xi=None
    
    for option in getoptions(state):
        state=copy.deepcopy(current_state)
        state=move(state,option)
        print(state)
        if(finish_game(state)):
            m=state[6]-state[13]
        elif depth==0:
            m=state[6]-state[13]
            print(m)
        elif state[14]==-1:
            m,_=mini(state,depth)
        elif state[14]==1:
            m,_=maxi(state,depth)
        if m < miniv:
            miniv = m
            xi = option


            
    return miniv,xi


def maxi(state,depth):
    depth-=1
    current_state=copy.deepcopy(state)
    maxiv=-49
    xi=None
        
    for option in getoptions(state):
        state=copy.deepcopy(current_state)
        state=move(state,option)
        print(state)
        if(finish_game(state)):
            m=state[6]-state[13]
        elif depth==0:
            m=state[6]-state[13]
            print(m)
        elif state[14]==-1:
            m,_mini(state,depth)
        elif state[14]==1:
            m,_=maxi(state,depth)
        if m > maxiv:
            maxiv = m
            xi = option


            
    return maxiv,xi