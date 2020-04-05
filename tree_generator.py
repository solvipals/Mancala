# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:27:57 2020

@author: andri
"""
from Board import move
from Game_Operations import finish_game

def state_list_generator(state):
    state_list=[]
    current_state=list(state)
    if len(state)==0:
        return [[],[],[],[],[],[]]
    if current_state[14]==1:
        for i in range(0,6):
            state=list(current_state)
            state=move(state,i)
            if state != []:
                finish_game(state)
            state_list.append(state)
    elif current_state[14]==-1:
        for i in range(7,13):
            state=list(current_state)
            state=move(state,i)
            if state != []:
                finish_game(state)
            state_list.append(state)
    state=list(current_state)
    return list(state_list)


def tree_state_generator(state,depth):
    states_tree=[[] for i in range(depth)]
    states_tree[0]=state_list_generator(state)
    for d in range(1,depth):
        for j in range(0,len(states_tree[d-1])):
            states_tree[d].extend(state_list_generator(states_tree[d-1][j]))
            
    return states_tree