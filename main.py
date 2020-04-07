# -*- coding: utf-8 -*-



#Eftir ad skrifa main 

import os 
from Board import *
print("Do you want to play against another player(0) or the computer(1)?")
game_type=-1
while game_type>1 or game_type<0:
    game_type=int(input())
    if game_type==0:
        os.system('2player.py')
    elif game_type==1:
        os.system('1player.py')
    else:
        print('Invalid input, please choose either 0 or 1')
    


print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print('%                                 %')
print('%%%%%%%%%%%  GAME OVER %%%%%%%%%%%%')
print('%                                 %')
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%') 