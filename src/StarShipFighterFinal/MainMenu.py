
import pygame
from StarShipFighterFinal.StarShipFighter import *
from StarShipFighterFinal.Fighter import *  
from pygame.locals import *

import sys

'''                       _____ _     _        ______ _       _     _____            
                    /  ___| |             /  ___| |   (_)       |  ___(_)     | |   | |            
                    \ `--.| |_ __ _ _ __  \ `--.| |__  _ _ __   | |_   _  __ _| |__ | |_ ___ _ __  
                     `--. \ __/ _` | '__|  `--. \ '_ \| | '_ \  |  _| | |/ _` | '_ \| __/ _ \ '__| 
                    /\__/ / || (_| | |    /\__/ / | | | | |_) | | |   | | (_| | | | | ||  __/ |    
                    \____/ \__\__,_|_|    \____/|_| |_|_| .__/  \_|   |_|\__, |_| |_|\__\___|_|    
                                                        | |               __/ |                    
                                                       |_|              |___/         
  Star Ship Fighter 1.2.3 is a fixed shooter python game develop by Jose Virgen. The objective of the game is to 
  score as many points as possible by destroying the enemies. The player controls a star ship fighter that can move left/right/up/down. 
  Enemies will begin to follow the player.Player must escape and destroy. Among the game, there will be abilites
  to power up and obtain a heavy gunner that the player can achieve.'''

class MainMenu(): 
    
    def mainGame(self):
        
        ########################################
        ##    Back Ground Settings            ## d
        ##                                    ## 
        ########################################
        
        pygame.init()  
        FPS = 30
        fpsClock = pygame.time.Clock()
        pygame.display.set_caption('Main Menu')
        
        window_size = (750, 500)
        screen = pygame.display.set_mode(window_size)
        Background = pygame.image.load("images/background.jpg").convert()
        screen.blit(Background,(0,0))
    
        screen.blit(Background,(0,0)) 
        font = pygame.font.SysFont('Buxton Sketch', 40, True, True)
        text = font.render("STARSHIP FIGHTER",True,Color(255,255,51))
        screen.blit(text, [200, 100])
        
        startFont = pygame.font.SysFont('Buxton Sketch', 16, True, True)
        startText = startFont.render('(Press Space Bar to Star Game)',True,Color(255,255,51))
        screen.blit(startText,[275,150])
        
        image = pygame.image.load('images/keyboard.png').convert()
        image.set_colorkey(pygame.Color(0,0,0))
        rect = image.get_rect()
        
        rect.x = 25
        rect.y = 300
        screen.blit(image,(rect.x,rect.y))
        
        
        image = pygame.image.load('images/HoldLeft.png').convert()
        image.set_colorkey(pygame.Color(0,0,0))
        rect = image.get_rect()
        rect.x = 600
        rect.y = 320
        screen.blit(image,(rect.x,rect  .y))
        
        fighter = Fighter(375,250)   
        fighter2 = Fighter(545,200)
        fighter3 = Fighter(200,200)
        
        while True:  # <--- main game loop
            for event in pygame.event.get():
                if event.type == QUIT:  # QUIT event to exit the game
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        start = StarShipFighter()
                        start.GAME()
                        
    
                fighter.draw(screen)
                fighter2.draw(screen)
                fighter3.draw(screen)
                pygame.display.update()      
                fpsClock.tick(FPS)   
               
                    
main = MainMenu()
main.mainGame()


