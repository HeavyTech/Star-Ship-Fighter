'''___  ___.  _______ .___________. _______   ______   .______      
|   \/   | |   ____||           ||   ____| /  __  \  |   _  \     
|  \  /  | |  |__   `---|  |----`|  |__   |  |  |  | |  |_)  |    
|  |\/|  | |   __|      |  |     |   __|  |  |  |  | |      /     
|  |  |  | |  |____     |  |     |  |____ |  `--'  | |  |\  \----.
|__|  |__| |_______|    |__|     |_______| \______/  | _| `._____| 
'''

import pygame
from pygame.locals import * 
class Meteor(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/meteor.png').convert()
        self.image.set_colorkey(pygame.Color(0,0,0))
        
        self.rect = self.image.get_rect()
        self.health = 6
    '''Draw
        Attributes: 
            Screen: Takes in the value of the screen
        Return:
            Function will blit the image onto screen'''     
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))
    '''updateMeteorHealth
        Return: int(health) value after being decremented'''
    def updateMeteorHealth(self):
        self.health = self.health - 3
    '''Returns current health'''
    def getHealth(self):
        return self.health    
    '''Sets the postion for meteor'''
    def update(self):
        self.rect.x = self.rect.x
        self.rect.y = self.rect.y 