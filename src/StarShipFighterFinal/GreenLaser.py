'''
Created on May 20, 2015

@author: Heavytech
'''
import pygame
from pygame.locals import * 

class GreenLaser(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/greenlaser.png').convert()
        self.image.set_colorkey(pygame.Color(0,0,0))
        self.rect = self.image.get_rect()
        
        
    def draw(self, screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))
    
    def update(self):
        self.rect.y +=10    