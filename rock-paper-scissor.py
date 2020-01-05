#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 22:08:51 2019

@author: jishanmsharif
"""

from random import randint

#The first step is to create a set of options the computer can choose from
t = ["Rock", "Paper", "Scissors"]

#the play made by the computer is random ensuring a fair game 
computer = t[randint(0,2)]

#set player to False
user = False

while user == False:
    if user == "x":
        break
#set player to True
    user = input("Rock, Paper, Scissors?")
    if user == computer:
        print("Tie!")
    elif user == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", user)
        else:
            print("You win!", user, "smashes", computer)
    elif user == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", user)
        else:
            print("You win!", user, "covers", computer)
    elif user == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", user)
        else:
            print("You win!", user, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #user was set to True, but we want it to be False so the loop continues
    user = False
    computer = t[randint(0,2)]