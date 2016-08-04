'''
Created on May 20, 2015

@author: Jose Virgen
'''
import pygame
from pygame.locals import * 

class BigExplosion(pygame.sprite.Sprite):
    def __init__(self,enemy):
        super().__init__()
        self.image = pygame.image.load('images/explosion.png').convert()
        self.image.set_colorkey(pygame.Color(0,0,0))
        
        self.rect = self.image.get_rect()
        self.rect.x = enemy.rect.x +3
        self.rect.y = enemy.rect.y
        
    def stop(self):
        self.rect.x = 0
        self.rect.y = 0 
        
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))
    
    def update(self):
        self.rect.x = self.rect.x
        self.rect.y = self.rect.y 
        