'''
Created on May 27, 2015
'''
import pygame
from pygame.locals import * 
import random
from random import randint
'''  _______  __    __  .__   __. .__   __.  _______ .______      
 /  _____||  |  |  | |  \ |  | |  \ |  | |   ____||   _  \     
|  |  __  |  |  |  | |   \|  | |   \|  | |  |__   |  |_)  |    
|  | |_ | |  |  |  | |  . `  | |  . `  | |   __|  |      /     
|  |__| | |  `--'  | |  |\   | |  |\   | |  |____ |  |\  \----.
 \______|  \______/  |__| \__| |__| \__| |_______|| _| `._____|'''
                                                               
class Gunner(pygame.sprite.Sprite):
    def __init__(self,x,y,vx,vy):
        super().__init__()
        self.image = pygame.image.load('images/powerup.png').convert()
        self.image.set_colorkey(pygame.Color(0,0,0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y 
        self.vx = vx
        self.vy = vy 
    '''Draw
        Attributes: 
            Screen: Takes in the value of the screen
        Return:
            Function will blit the image onto screen'''  
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))   
        
    '''Move 
            Function will detect collision between size of the screen
            if collision occurs, then make the power up bounce back'''   
    def move(self,screen):
        r_collide = self.rect.x + self.image.get_width() + self.vx > screen.get_width()
        l_collide = self.rect.x + self.vx < 0
        t_collide = self.rect.y + self.vy < 0
        b_collide = self.rect.y + self.image.get_height() + self.vy > screen.get_height()

        # Check collision on right and left sides of screen
        if l_collide or r_collide:
            self.vx *=-1

        # Check collision on top and bottom sides of screen
        if t_collide or b_collide:
            self.vy *= -1

        self.rect.x += self.vx
        self.rect.y += self.vy
    '''Random Location
            Function will assign a random value for (x,Y) coordinates'''  
    def randomLocation(self,screen): 
 
        randomX = randint(0,750) 
        randomY = randint(0,420)
        self.rect.x = randomX
        self.rect.y = randomY
        screen.blit(self.image,(self.rect.x,self.rect.y))