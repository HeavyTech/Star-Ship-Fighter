'''
Created on May 20, 2015

@author: Jose Virgen
'''
import pygame
from pygame.locals import * 


'''__    __   _______     ___       __      .___________. __    __     .______        ___      .______      
|  |  |  | |   ____|   /   \     |  |     |           ||  |  |  |    |   _  \      /   \     |   _  \     
|  |__|  | |  |__     /  ^  \    |  |     `---|  |----`|  |__|  |    |  |_)  |    /  ^  \    |  |_)  |    
|   __   | |   __|   /  /_\  \   |  |         |  |     |   __   |    |   _  <    /  /_\  \   |      /     
|  |  |  | |  |____ /  _____  \  |  `----.    |  |     |  |  |  |    |  |_)  |  /  _____  \  |  |\  \----.
|__|  |__| |_______/__/     \__\ |_______|    |__|     |__|  |__|    |______/  /__/     \__\ | _| `._____|'''

class HealthBar():
    def __init__(self,screen,x,y):
        super().__init__()
        
        self.screen = screen
        self.x = x
        self.y = y 

        #Locations of Health bar
        self.top_left = (7,479)
        self.bottom_left = ( 7, 484)
       
        self.top_right = (100,479)
        self.bottom_right = (100,484)
       
        self.height = abs(self.top_left[1] - self.bottom_left[1])
        self.width  = abs(self.top_left[0] - self.top_right[0])
        
        self.color = (186,0,0)
        
        self.max_health= self.width
        self.health = 100
        
    '''Increase Health
        Attributes:
            Amount: int(amount) Takes in a inter amount
        Returns:
            Function will update the health given by amount'''
    def increase_health(self,amount):
        self.health +=amount 
        if self.health > self.max_health : 
            self.health = self.max_health
        '''Decrease Health
        Attributes:
            Amount: int(amount) Takes in a inter amount
        Returns:
            Function will update the health given by amount'''     
    def decrease_health(self,amount):
        self.health -= amount
        if self.health < 0 :
            self.health = 0     
    '''Draw
        Attributes:
            draw: This will draw and render the updated health at anytime'''
    def draw(self):
        if self.health !=0:
            
            bar = pygame.Rect(self.top_left[0],
                              self.top_left[1],
                              self.health,
                              self.height)
            pygame.draw.rect(self.screen, self.color, bar, 5)
          
