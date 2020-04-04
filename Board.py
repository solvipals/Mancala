# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 14:29:15 2020

@author: SOPA
"""

import numpy as np
import pandas as pd


def initialize_game():
    state=[4,4,4,4,4,4,0,4,4,4,4,4,4,0]
    p1=True
    index=0
    return state,p1,index


def print_board(state,state_score):
    print("|--"+ str(state[12])+"--" +str(state[11])+"--" +str(state[10])+"--" +str(state[9])+"--" +str(state[8])+"--" +str(state[7])+"--|""\n" 
      +"|" +str(state[13])+"------------------" +str(state[6])+"|\n"
      "|--"+ str(state[0])+"--" +str(state[1])+"--" +str(state[2])+"--" +str(state[3])+"--" +str(state[4])+"--" +str(state[5])+"--|")
    print("The score of the board is:" + str(state_score) )
    if p1==True:
        print("Player 1's turn")
    elif p1==False:
        print("Player2's turn")
        
    

def move(state,p1,index):
    if index==6 or index >= 13:
        print('Unvalid move')
        state_score=state[6]-state[13]
        return state,p1,state_score
    elif state[index]==0:
        print('The cup is empty')
        state_score=state[6]-state[13]
        return state,p1,state_score
    elif index>13:
        index=index-13
    pebble_count=state[index]
    state[index]=0
    if p1==True:
        while pebble_count>0:
            index+=1
            if index ==13:
                index=0
            state[index]+=1
            pebble_count-=1
    elif p1==False:
        while pebble_count>0:
            index+=1
            if index==6:
                index+=1
            if index >13:
                index=0
            state[index]+=1
            pebble_count-=1
    if p1==True and index==6:
        p1=True
    elif p1==True:
        p1=False
    elif p1==False and index==13:
        p1=False
    elif p1==False:
        p1=True
    state_score=state[6]-state[13]
    return state,p1,state_score



def best_move(state,state_score):
    current_state=list(state)
    best_index=7
    best_score=state_score
    for i in range(7,13):
        state=list(current_state)
        state,p1,score=move(state,False,i)
        if score<best_score:
            best_score=score
            best_index=i
    print(best_index,best_score)
    return best_index,best_score

