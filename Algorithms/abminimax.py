
from Board import *
import copy


def mini(state,depth, alpha, beta):
    depth-=1
    current_state=copy.deepcopy(state)
    miniv=49
    xi=None
    m=None 
    for option in getoptions(state):
        state=copy.deepcopy(current_state)
        state=move(state,option)
        if(finish_game(state)):
            m=state[6]-state[13]
        elif depth==0:
            m=state[6]-state[13]
        elif state[14]==-1:
            (m,_)=mini(state,depth, alpha, beta)
        elif state[14]==1:
            (m,_)=maxi(state,depth, alpha, beta)
            
        if m < miniv:
            miniv = m
            xi = option
        
        #state = current_state
        if miniv <= alpha:
            return miniv, xi
        
        if miniv < beta:
            beta = miniv
            
    return miniv,xi


def maxi(state,depth, alpha, beta):
    depth-=1
    current_state=copy.deepcopy(state)
    maxiv=-49
    xi=None
    m=None    
    for option in getoptions(state):
        state=copy.deepcopy(current_state)
        state=move(state,option)
        if(finish_game(state)):
            m = state[6]-state[13]
        elif depth==0:
            m=state[6]-state[13]
        elif state[14]==-1:
            (m,_)=mini(state,depth, alpha, beta)
        elif state[14]==1:
            (m,_)=maxi(state,depth, alpha, beta)
            
        if m > maxiv:
            maxiv = m
            xi = option
        
        #state = current_state
        
        if maxiv >= beta:
            return maxiv, xi
        
        if maxiv > alpha:
            alpha = maxiv

            
    return maxiv,xi