# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 01:36:03 2020

@author: SOPA
"""



import pandas as pd
from zeroplayer import *
from Board import *
from abminimax import *
from defaultminimax import *


# dataframe Name and Age columns
df = pd.DataFrame({'Depth': [1,2,3,4,5,6,7,8,9,10]})

data = []

for i in range (1,11):
    state = initialize_game()
    
    start = time.time()
    best_score,best_move = minidef(state,i)
    end = time.time()
    thinkingtime = round(end - start, 7)
    data.append(thinkingtime)  
    # print(data)
    
df["Default minimax"] = data

data = []

for i in range (1,11):

    state = initialize_game()
    start = time.time()
    best_score,best_move = mini(state,i, -49, 49)
    end = time.time()
    thinkingtime = round(end - start, 7)
    data.append(thinkingtime)  
    # print(data)
df["MiniMax AB"] = data
 
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('tests.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='minimax vs minimaxAB - time', index=False)

# Close the Pandas Excel writer and output the Excel file.
writer.save()