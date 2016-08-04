
'''
Created on May 6, 2015

@author: Heavytech
'''

import pygame
from pygame.locals import * 
import math
from random import  randrange
from StarShipFighterFinal.GreenLaser import GreenLaser

class smallEnemy(pygame.sprite.Sprite):
 
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('images/playerShip3_blue.png').convert()
        self.image.set_colorkey(pygame.Color(0,0,0))
        self.rect = self.image.get_rect() 
        
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0 
        self.change_y = 0 

        self.health = 50
        
    def updateHealth(self):
        self.health = self.health - 10
        
    def getHealth(self):
        return self.health

    def update(self) :
        self.rect.x = self.change_x
        self.rect.y = self.change_y
           
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))
        
    def enemyShoot(self,greenBullet): 
        greenBullet.rect.y +=10