# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 22:18:41 2020

@author: SOPA
"""


import pandas as pd
from zeroplayer import *
from Board import *
from abminimax import *

# dataframe Name and Age columns
df = pd.DataFrame({'Depth': [1,2,3]})


for i in range (1,4):
    data = []
    for j in range(1,4):
        state  = initialize_game()
        while (not finish_game(state)):
            if state[14]==1:
                best_score,best_move = maxi(state,i, -49, 49)
                move(state,best_move)
        
            elif state[14]==-1:
                best_score,best_move = mini(state,j, -49, 49)
                move(state,best_move)
                #print("Player2's turn")
    
        score = state[6] - state[13]
        data.append(score)
    print(i)    
    # print(data)
    df[i] = data

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('tests.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Minimax AB vs MiniMax AB', index=False)

# Close the Pandas Excel writer and output the Excel file.
writer.save()


# import pandas as pd
# from openpyxl import load_workbook
# # new dataframe with same columns
# df = pd.DataFrame({1, 2, 3, 4, 'Age': [100,70,40,60]})
# writer = pd.ExcelWriter('demo.xlsx', engine='openpyxl')
# # try to open an existing workbook
# writer.book = load_workbook('demo.xlsx')
# # copy existing sheets
# writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
# # read existing file
# reader = pd.read_excel(r'demo.xlsx')
# # write out the new sheet
# df.to_excel(writer,index=False,header=False,startrow=len(reader)+1)

# writer.close()