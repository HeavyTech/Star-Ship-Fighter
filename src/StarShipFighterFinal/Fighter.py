'''
Created on May 6, 2015

@author: Jose Virgen
'''


import pygame
from pygame.locals import * 
from random import  randrange
from StarShipFighterFinal.Bullet import * 
from StarShipFighterFinal.Gunner import * 


class Fighter(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('images/playerShip1_red.png').convert()
        self.image.set_colorkey(pygame.Color(0,0,0))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0 
        self.change_y = 0
        self.health = 100
        self.maxHealth = 100
    
    
    '''Draw
        Attributes: 
            Screen: Takes in the value of the screen
        Return:
            Function will blit the image onto screen'''
        
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))
        
        '''updateHealth
        Attributes: 
            Screen: Takes in the value of the screen
            function will decrement the value of health 
        Return:
            Function will return an update on the health '''    
        
    def updateHealth(self):
        self.health = self.health - 10
    '''Gain Health
            Return:
                This will return the health if powerup has been given'''
    def gainHealth(self):
        self.health = self.health + 25
        if self.health >= self.maxHealth:
            self.health = self.maxHealth
    '''getHealth
        Returns: int(Health) Value'''
    def getHealth(self):
        return self.health   
    '''   Movement of the Player
                           Move up : Fighter will be allowed to up in the Y-coordinate 
                           Move Down: Fighter will be allowd to down in the Y-coordinate 
                           Move Right : Fighter will be allowed to up in the X -coordinate 
                           Move Left : Fighter will be allowd to up in the X-coordinate 
                           Move Stop : Player will will main the remaining location given by movement'''
    def move_left(self,screen): 
        l_collision = self.rect.x
        
        if l_collision <= 0:
            self.change_x = 0
        else:    
            self.change_x = -5
            
    def move_right(self,screen):
            
        r_collision = self.rect.x 
        
        if r_collision >= screen.get_width() :  # SCREEN WIDTH
            self.change_x = 0 
        else:    
            self.change_x = 5

        
    def move_up(self):
        self.change_y = -5
        
    def move_down(self):
        self.change_y = 5      
        
    def stop(self):
        self.change_x = 0
        self.change_y = 0
        
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        
    '''Create  Guns
            Attributes: 
                bullet 1 : Takes in one bullet object
            Returns : 
                Will Adjust a  bullet objects in the Star Ship Fighter'''           
    def createGun(self,bullet):
        bullet.rect.x = self.rect.x + 13
        bullet.rect.y = self.rect.y - 20
    '''Create Two Guns
            Attributes: 
                bullet 1 & 2 : Takes in two bullet object
            Returns : 
                Will Adjust two bullet objects in the Star Ship Fighter'''
        
    def twoGuns(self,bullet,bullet2):
    
        bullet.rect.x = self.rect.x + 20
        bullet.rect.y = self.rect.y -20
        
        bullet2.rect.x = self.rect.x 
        bullet2.rect.y = self.rect.y 
            
    
            
        
            