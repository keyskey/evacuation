#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 13:44:28 2018

@author: rte28
"""

import numpy as np

g = 0.1        #0.383
ks = 5.5

#time_ratio = 1/3.2  #[s/step]    

class Agent:

    def __init__(self, x, y):
        self.posx = x
        self.posy = y
        self.nextx = None
        self.nexty = None
        self.Smnlist = []        
        self.CanMove = True   
    
    def SetPosition(self, x, y):
        self.posx = x
        self.posy = y

    def SetNext(self, x, y):
        self.nextX = x
        self.nextY = y
                 
    def Pkl(self, Skl, Smnlist):
        """
        With this probability, determine the direction of next step
        """
        under = 0.0
        up = np.exp(-ks*Skl)

        for s in Smnlist:
            under += np.exp(-ks*s)  
            
        up = up/under
        
        return up
            
    def uk(self, k):
        """
        With this probability, collisioners can avoid crash and randomely chosen agent can move
        """
        u = (1-g)**k + k*g*(1-g)**(k-1)
        
        return u
    
    
