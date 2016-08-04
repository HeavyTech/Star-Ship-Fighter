import pygame
from pygame.locals import * 
import random
from StarShipFighterFinal.Bullet import Bullet
from StarShipFighterFinal.Enemy import Enemy
from StarShipFighterFinal.Fighter import Fighter
from StarShipFighterFinal.BigExplosion import BigExplosion
from StarShipFighterFinal.SmallExplosion import SmallExplosion
import sys

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

def generate_sprites(block_list, all_sprites_list, screen_w, screen_h, num):
    for i in range(num):
        if i % 2 == 0:
            enemy = Enemy()
            enemy.rect.x = random.randrange(screen_w)
            enemy.rect.y = random.randrange(screen_h)
            block_list.add(enemy)
            all_sprites_list.add(enemy)

def main():
    
    pygame.init()
    FPS = 30 
    fpsClock = pygame.time.Clock()
    pygame.display.set_caption('StarShip Fighter')
    
    #--------Gathering Sounds---------#
    laserSound = pygame.mixer.Sound('Sounds/laser5.ogg')
    pygame.mixer.music.load('Sounds/Deepspace_lazers.ogg')
    explosionSound = pygame.mixer.Sound('Sounds/BombExploding.ogg')
    pygame.mixer.music.set_endevent(USEREVENT)
    #pygame.mixer.music.play()
    

   
    #--------Setting BackGround--------#
    window_size = (500, 500)
    screen = pygame.display.set_mode(window_size)
    Background = pygame.image.load("images/blue.jpg").convert()
    screen.blit(Background,(0,0))

    allSprite = pygame.sprite.Group()
    enemyList = pygame.sprite.Group()
    bulletList = pygame.sprite.Group()
    #----------------------------------#

    #---------Setting up Player----------#
    fighter = Fighter(250,450)
    fighter.draw(screen)
    allSprite.add(fighter)
    
    #---------Setting up Enemy------------#
    enemy = Enemy()
    enemy.draw(screen)
    enemyList.add(enemy)
    
    generate_sprites(enemyList, allSprite, SCREEN_WIDTH, SCREEN_HEIGHT, 10)
    score = 0
    while True: 
        for event in pygame.event.get():
            if event.type == QUIT: 
                pygame.quit()
                sys.exit()
            
            if event.type == USEREVENT:
                pygame.mixer.music.play()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                bullet = Bullet()
                bullet.rect.x = fighter.rect.x + 13
                bullet.rect.y = fighter.rect.y - 20
                laserSound.play()
                allSprite.add(bullet)
                bulletList.add(bullet)  
                
                
                      
            #---------Movement of Players--------------#
            if event.type == pygame.KEYDOWN:
                if event.key == K_w:
                    fighter.move_up()
                if event.key == K_s:
                    fighter.move_down()
                if event.key == K_a:
                    fighter.move_left()
                if event.key == K_d:
                    fighter.move_right()
                if event.key == K_p:
                    pygame.time.wait(3000)
                       
                    
            if event.type == pygame.KEYUP:
                if event.key == K_w:
                    fighter.stop()
                if event.key == K_s:
                    fighter.stop()
                if event.key == K_a:
                    fighter.stop()
                if event.key == K_d:
                    fighter.stop()
              
                
    
    
        #------After kep Events-----# 
        screen.blit(Background,(0,0))
        fighter.update()
        fighter.draw(screen)
        allSprite.update()            
        allSprite.draw(screen)   
        
    
        #----------GAME LOGIC------------#
        for bullet in bulletList:
            blockEnemyList = pygame.sprite.spritecollide(bullet, enemyList, False)
            
            
            for enemy in blockEnemyList:
                explosion = SmallExplosion(enemy)
                explosion.draw(screen)
                print('You been hit!!')
                bulletList.remove(bullet)
                allSprite.remove(bullet)
                enemy.updateHealth()
                print(enemy.getHealth())
                
                #----------ENEMY DOWN----------#
                #                              #
                #------------------------------#
                if enemy.getHealth() <= 0:
                    explosionSound.play()
                    bigExplosion = BigExplosion(enemy)
                    bigExplosion.draw(screen)
                    enemyList.remove(enemy)
                    allSprite.remove(enemy)
                    score = score + 10
    
                    print('Enemy has been destroyed!')
                    print('Score',score)
        
        allSprite.update()
        pygame.display.update()      
        fpsClock.tick(FPS)     
    
        
if __name__ == "__main__":
    main()    