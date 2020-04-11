# -*- coding: utf-8 -*-



#Eftir ad skrifa main 

import os 
from Board import *

q = False


while not q:
    print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
    print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
    print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
    print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤                                           ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
    print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤                                           ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
    print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤             LET'S PLAY MANCALA            ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
    print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤                                           ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
    print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤                                           ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
    print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
    print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
    print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
    
    print(" ")
    print(" ")
    
    print("Do you want to play against another player(0) or the computer(1)?")
    print("We have 3 kinds of variation you can play.")
    print(" ")
    print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
    print(" ")
    print("For 1 Player game - Choose 1")
    print("For 2 Player game - Choose 2")
    print("To watch the computer play against it self - Choose 3")
    print(" ")
    print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
    print(" ")
    
    validInput = False
    while not validInput:
        
        choice=input("Choose your game variation :    ")
        try:
           choice = int(choice)
           try:
               if (choice>=1 and choice<=3):
                   validInput = True
               else:
                   raise Exception 
           except Exception:
                print("Invalid Choice. You must select either 1, 2 or 3")
        except ValueError:
            print("Only integers are allowed, please choose again!")
    
    
    
    if choice == 1:
        os.system('1player_minimax.py')
    elif choice == 2:
        os.system('2player.py')
    elif choice == 3:
        os.system('0player.py')
    
    print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
    print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
    print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
    print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤                                           ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
    print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤                                           ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
    print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤        GAME OVER        ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
    print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤                                           ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
    print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤                                           ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
    print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
    print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
    print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
    
    validInput = False
    while not validInput:
        print(" ")
        print(" ")
        print("Would you like to play again???")
        
        choice = input("1 = YES         0 = NO:         ")
        print(" ")
        try:
           choice = int(choice)
           try:
               if (choice == 1):
                   validInput = True
               elif (choice == 0):
                   validInput = True
                   q = True
               else:
                   raise Exception 
           except Exception:
                print("Invalid Choice. Input can only be 0 or 1")
                
        except ValueError:
            print("Only integers are allowed, please choose again!")

