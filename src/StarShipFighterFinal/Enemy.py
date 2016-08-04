'''______ .__   __.  _______ .___  ___. ____    ____ 
|   ____||  \ |  | |   ____||   \/   | \   \  /   / 
|  |__   |   \|  | |  |__   |  \  /  |  \   \/   /  
|   __|  |  . `  | |   __|  |  |\/|  |   \_    _/   
|  |____ |  |\   | |  |____ |  |  |  |     |  |     
|_______||__| \__| |_______||__|  |__|     |__|'''

import pygame
from pygame.locals import * 
import math
from random import  randrange
'''Enemy
        This holds all the functions the enemy has
        
        Attributes: 
            updatehealth - this function will decrement the value of health for each enemey
            getHealth: Returns int(health) the remaining health of enemy
            move: Controls the movement of the enemy. Which will follow the player
            update : This will update the image for every action there is
            draw: This will blit the image on to the screen'''
        
    
class Enemy(pygame.sprite.Sprite):
 
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/playerShip3_green.png').convert()
        self.image.set_colorkey(pygame.Color(0,0,0))
        self.rect = self.image.get_rect() 
        self.change_x = 0 
        self.change_y = 0 

        self.health = 50
        
    def updateHealth(self):
        self.health = self.health - 10
        
    def getHealth(self):
        return self.health
    
    def move(self,fighter,speed):
        px = fighter.rect.x
        py = fighter.rect.y 
         
        
        if self.rect.x > px:
            self.change_x = -speed
   
        elif self.rect.x < px:
            self.change_x = speed
              
        if self.rect.y > py:
            self.change_y = -speed
           
        elif self.rect.y < py:
            self.change_y = speed

    def stop(self):
        self.change_x = 0
        self.change_y = 0
        
    def update(self) :
        self.rect.x += self.change_x
        self.rect.y += self.change_y
              
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))