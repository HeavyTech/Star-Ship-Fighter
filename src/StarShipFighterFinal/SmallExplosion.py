'''
Created on May 20, 2015

@author: Jose Virgen
'''
import pygame
from pygame.locals import * 

class SmallExplosion(pygame.sprite.Sprite):
    def __init__(self,enemy):
        super().__init__()
        self.image = pygame.image.load('images/Smallexplosion.png').convert()
        self.image.set_colorkey(pygame.Color(0,0,0))
        
        self.rect = self.image.get_rect()
        
        self.rect.x = enemy.rect.x
        self.rect.y = enemy.rect.y

    
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))