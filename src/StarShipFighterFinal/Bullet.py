'''
Created on May 6, 2015

@author: Jose Virgen
'''
import pygame
from random import  randrange
'''
.______    __    __   __       __       _______ .___________.
|   _  \  |  |  |  | |  |     |  |     |   ____||           |
|  |_)  | |  |  |  | |  |     |  |     |  |__   `---|  |----`
|   _  <  |  |  |  | |  |     |  |     |   __|      |  |     
|  |_)  | |  `--'  | |  `----.|  `----.|  |____     |  |     
|______/   \______/  |_______||_______||_______|    |__|   '''
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/laserRed01.png').convert()
        self.image.set_colorkey(pygame.Color(0,0,0))
        
        self.rect = self.image.get_rect()
    '''Draw
        Function Blits the image onto screen'''
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))
    '''Update
        Bullet will be moving -10 in the y direction'''
    def update(self):
        self.rect.y -=10
        