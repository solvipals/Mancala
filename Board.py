# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 14:29:15 2020

@author: SOPA
"""

import numpy as np, pandas as pd

def initialize_game():
    state = [
     4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0, 1]
    return state


def print_state(state):
    print('|--' + str(state[12]) + '--' + str(state[11]) + '--' + str(state[10]) + '--' + str(state[9]) + '--' + str(state[8]) + '--' + str(state[7]) + '--|\n' + '|' + str(state[13]) + '------------------' + str(state[6]) + '|\n|--' + str(state[0]) + '--' + str(state[1]) + '--' + str(state[2]) + '--' + str(state[3]) + '--' + str(state[4]) + '--' + str(state[5]) + '--|')
    print('The score of the board is:' + str(state[6] - state[13]))


def move(state, index):
    if index in getoptions(state):
        pebble_count = state[index]
        state[index] = 0
    else:
        return []
    if state[14] == 1:
        while pebble_count > 0:
            index += 1
            if index == 13:
                index = 0
            state[index] += 1
            pebble_count -= 1

        if index in (0, 1, 2, 3, 4, 5):
            if state[index] == 1:
                if state[abs(index - 12)] != 0:
                    state[6] += 1 + state[(12 - index)]
                    state[index] = 0
                    state[abs(index - 12)] = 0
                    
    elif state[14] == -1:
        while pebble_count > 0:
            index += 1
            if index == 6:
                index += 1
            if index > 13:
                index = 0
            state[index] += 1
            pebble_count -= 1

        if index in (7, 8, 9, 10, 11, 12) and state[index] == 1:
            if state[(12 - index)] != 0:
                state[13] += 1 + state[(12 - index)]
                state[index] = 0
                state[12 - index] = 0
    if state[14] == 1 and index == 6:
        state[14] = 1
    elif state[14] == 1:
        state[14] = -1
    elif state[14] == -1 and index == 13:
        state[14] = -1
    elif state[14] == -1:
        state[14] = 1
    return state


def getoptions(state):
    options = []
    if state[14] == 1:
        for i in range(6):
            if state[i] != 0:
                options.append(i)

        return options
    if state[14] == -1:
        for i in range(7, 13):
            if state[i] != 0:
                options.append(i)

        return options
    
        



