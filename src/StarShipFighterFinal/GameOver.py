
import pygame
from pygame.locals import *
import sys
'''  _______      ___      .___  ___.  _______      ______   ____    ____  _______ .______      
 /  _____|    /   \     |   \/   | |   ____|    /  __  \  \   \  /   / |   ____||   _  \     
|  |  __     /  ^  \    |  \  /  | |  |__      |  |  |  |  \   \/   /  |  |__   |  |_)  |    
|  | |_ |   /  /_\  \   |  |\/|  | |   __|     |  |  |  |   \      /   |   __|  |      /     
|  |__| |  /  _____  \  |  |  |  | |  |____    |  `--'  |    \    /    |  |____ |  |\  \----.
 \______| /__/     \__\ |__|  |__| |_______|    \______/      \__/     |_______|| _| `._____|

This class will display the Game Over window
It will Blit the original screen'''
class GameOver(): 
    
    def Over(self):
        
        pygame.init()  
        FPS = 30
        fpsClock = pygame.time.Clock()
        pygame.display.set_caption('Game Over')
        
        window_size = (750, 500)
        screen = pygame.display.set_mode(window_size)
        Background = pygame.image.load("images/background.jpg").convert()
        screen.blit(Background,(0,0))
    
        screen.blit(Background,(0,0)) 
        font = pygame.font.SysFont('Buxton Sketch', 40, True, True)
        text = font.render("GAME OVER",True,Color(255,255,51))
        screen.blit(text, [250, 250])
        gameOverSound = pygame.mixer.Sound('Sounds/GAME_OVER.ogg')
        gameOverSound.play()
        
        while True:  # <--- main game loop
            for event in pygame.event.get():
                if event.type == QUIT:  # QUIT event to exit the game
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print('Your Lame')
            
            pygame.display.update()      
            fpsClock.tick(FPS)   
               
                
