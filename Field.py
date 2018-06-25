#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 13:42:51 2018

@author: rte28
"""

import numpy as np
import random as rnd
import csv
from Agent import Agent

num_people = 20

class Cell:
    def __init__(self, num):
        self.num = num
        self.exist = False
    
class Field(Agent, Cell):
      
    def __init__(self, file):
        self.field = np.genfromtxt(file, delimiter=",")
        self.columns = self.field.shape[1]                                       # Number of column
        self.rows = self.field.shape[0]                                          # Number of row
        self.agents = []

        """
        Change the coordinate from Python array's index to cartesian
        """
        self.cells = np.array([[Cell(self.field[self.rows-1-y, self.columns-1-x]) for x in range(self.columns)] for y in range(self.rows)])

        while len(self.agents) < num_people:
            x = rnd.randint(0, self.columns-1)
            y = rnd.randint(0, self.rows-1)
            
            if self.cells[y,x].num > 0 and self.cells[y,x].exist == False:
                self.agents.append(Agent(x, y))
                self.cells[y,x].exist = True
        
        
    def Rand(self, probability):
        return rnd.random() < probability

    def search(self):
        
        for agent in self.agents:
            x = agent.posx
            y = agent.posy
            agent.Smnlist = []
            agent.Smnlist.append(self.cells[y,x].num)   
            agent.SetNext(x,y)

            """
            Search the surrounfing cells
            """
            right = self.columns
            up = self.rows

            if y+1 < up and self.cells[y+1,x].num != -1:                                   # up
                agent.Smnlist.append(self.cells[y+1,x].num)

            if y-1 > -1 and self.cells[y-1,x].num != -1:                                   # down
                agent.Smnlist.append(self.cells[y-1,x].num)
            
            if x-1 > -1 and y-1 > -1 and self.cells[y-1,x-1].num !=-1:                     # lower left
                agent.Smnlist.append(self.cells[y-1,x-1].num)
                
            if x+1 < right and y-1>-1 and self.cells[y-1,x+1].num != -1:                   # lower right
                agent.Smnlist.append(self.cells[y-1,x+1].num)
                
            if x-1 > -1 and self.cells[y,x-1].num != -1:                                   # left
                agent.Smnlist.append(self.cells[y,x-1].num)
                
            if x+1 < right and self.cells[y,x+1].num != -1:                                # right
                agent.Smnlist.append(self.cells[y,x+1].num)
                
            if x-1 > -1 and y+1 < up and self.cells[y+1,x-1].num != -1:                    # upper left
                agent.Smnlist.append(self.cells[y+1,x-1].num)
                 
            if x+1 < right and y+1 < up and self.cells[y+1,x+1].num != -1:                 # upper right
                agent.Smnlist.append(self.cells[y+1,x+1].num)
            
            """
            Determine the direction for next step
            """
            if y+1 < up and self.cells[y+1,x].num != -1 and self.Rand(agent.Pkl(self.cells[y+1,x].num, agent.Smnlist)):                        # up
                agent.SetNext(x,y+1)
                
            elif y-1 > -1 and self.cells[y-1,x].num != -1 and self.Rand(agent.Pkl(self.cells[y-1,x].num, agent.Smnlist)):                      # down
                agent.SetNext(x,y-1)

            elif x-1 > -1 and y-1 > -1 and self.cells[y-1,x-1].num != -1 and self.Rand(agent.Pkl(self.cells[y-1,x-1].num, agent.Smnlist)):     # Lower left
                agent.SetNext(x-1,y-1)
            
            elif x+1 < right and y-1 > -1 and self.cells[y-1,x+1].num != -1 and self.Rand(agent.Pkl(self.cells[y-1,x+1].num, agent.Smnlist)):  # lower right
                agent.SetNext(x+1,y-1)
                
            elif x-1 > -1 and self.cells[y,x-1].num != -1 and self.Rand(agent.Pkl(self.cells[y,x-1].num, agent.Smnlist)):                      # left
                agent.SetNext(x-1,y)
                
            elif x+1 < right and self.cells[y,x+1].num != -1 and self.Rand(agent.Pkl(self.cells[y,x+1].num, agent.Smnlist)):                   # right
                agent.SetNext(x+1,y)
                
            elif x-1 > -1 and y+1 < up and self.cells[y+1,x-1].num != -1 and self.Rand(agent.Pkl(self.cells[y+1,x-1].num, agent.Smnlist)):     # upper left
                agent.SetNext(x-1,y+1)
                
            elif x+1 < right and y+1 < up and self.cells[y+1,x+1].num != -1 and self.Rand(agent.Pkl(self.cells[y+1,x+1].num, agent.Smnlist)):  # upper right
                agent.SetNext(x+1,y+1)
            
    def SearchCollision(self):

        for focal in self.agents:
            focal.CanMove = True   # initialization

        """
        Check if focal is going to where the other agent already exists
        """
        for focal in self.agents:
            for opp in self.agents:
                if opp != focal and focal.nextx == opp.posx and focal.nexty == opp.posy:   
                    focal.CanMove = False
                  

        """
        Determine which agent can move in case there is collision
        """
        
        for focal in self.agents:
            if focal.CanMove == True:
                collisioners = [agent for agent in self.agents if agent.nextx == focal.nextx and agent.nexty == focal.nexty]  # Include focal itself
                AvoidCollision = False
                
            if len(collisioners) == 1:                                          # If no collisioners with focal agent 
                focal.CanMove == True

            else:                                                               # If more than 2 collisioners
                AvoidCollision = self.Rand(focal.uk(len(collisioners)))         # Whether focal can avoid collision and can move or not
                if AvoidCollision == True:
                    winner = rnd.choice(collisioners)                           # Randomely choose the agent who can move
                    winner.CanMove = True
                    collisioners.remove(winner)
                    for looser in collisioners:
                        looser.CanMove = False
                            
                else:                                                           # If can't avoid collision
                    for looser in collisioners:
                        looser.CanMove = False
   
    def escape(self):
        for focal in self.agents:
            if self.cells[focal.nextY, focal.nextX].num == 0:                   # num = 0 is the exit cell
                self.agents.remove(focal)
            
    def MovePosition(self):
        for focal in self.agents:
            if focal.CanMove == True:
                focal.SetPosition(focal.nextX, focal.nextY)
                                
            else: 
                focal.SetPosition(focal.posx, focal.posy)                       #Stay at the same position
        
    def move(self):
        self.search()
        self.SearchCollision()
        self.escape()
        self.MovePosition()
        
    def run(self):
        time = 0
        #for time in range(100):
        while len(self.agents) != 0:                                             # Continue until all agents finish escaping

            # Setting for output
            filename = 'output{}.csv'.format(time)
            f = open(filename, 'w')        
            header = ['X', 'Y', 'People']
            writer = csv.writer(f)
            writer.writerow(header)

            print("Timestep:", time, "Number of pedestrian:", len(self.agents))
            print((num_people-len(self.agents))/num_people*100, "% of the people has escaped")
            
            for x in range(self.columns):
                for y in range(self.rows):

                    exist = 0
                    for focal in self.agents:
                        if x == focal.posx and y == focal.posy:
                            exist = 5

                        elif self.cells[y,x].num == -1:    # Obstacle or wall
                            exist = 10 

                    writer.writerow([x,y,exist])

            self.move()              
            time += 1
            f.close() 

        filename = 'output{}.csv'.format(time)
        f = open(filename, 'w')        
        header = ['X', 'Y', 'People']
        writer = csv.writer(f)
        writer.writerow(header)

        # Output of final timestep
        for x in range(self.columns):
            for y in range(self.rows):
                if self.cells[y,x].num == -1:    # Obstacle or wall
                    writer.writerow([x,y,10])


        print("Timestep:", time, "Number of pedestrian:", len(self.agents))
        print((num_people-len(self.agents))/num_people*100, "% of the people has escaped")
        print("Finish evacuation !!")
       
def main():
    f = Field('field.csv')                   # Set the csv file which draw the field map
    f.run()
    
if __name__ == "__main__":
    main()
