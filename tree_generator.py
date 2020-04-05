# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:27:57 2020

@author: andri
"""
import numpy as np
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

def score_tree_generator(states_tree,depth):
    score_tree=[[] for i in range(depth)]
    d=(depth-1)
    print(d)
    #Computing socres for last level of score_tree
    for i in range(len(states_tree[d])):
        if states_tree[d][i]==[]:
            score_tree[d].append(np.nan)
        else:
            score_tree[d].append(states_tree[d][i][6]-states_tree[d][i][13])
    ## filling up rest of the tree with min(scores) when player -1 chooses and max when its player1's turn
    for j in range((d-1),-1,-1):
        print(j)
        for i in range(len(states_tree[j])):
            if states_tree[j][i]==[]:
                score_tree[j].append(np.nan)
            elif len(np.isnan(score_tree[j+1][(6*i):((6*i)+6)]))==6:
                score_tree[j].append(states_tree[j][i][6]-states_tree[j][i][13])
            #if its player 1's turn    
            elif states_tree[j][i][14]==1:
                score_tree[j].append(np.nanmax(score_tree[j+1][(6*i):((6*i)+6)]))
            #player 2s turn
            elif states_tree[j][i][14]==-1:
                score_tree[j].append(np.nanmin(score_tree[j+1][(6*i):((6*i)+6)]))
    return score_tree 
    