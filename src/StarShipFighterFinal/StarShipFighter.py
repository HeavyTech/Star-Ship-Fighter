import pygame
from pygame.locals import * 
from StarShipFighterFinal.BigExplosion import BigExplosion
from StarShipFighterFinal.SmallExplosion import SmallExplosion
from StarShipFighterFinal.Bullet import Bullet
from StarShipFighterFinal.Enemy import Enemy
from StarShipFighterFinal.Fighter import Fighter
from StarShipFighterFinal.HealthBar import HealthBar
from StarShipFighterFinal.Meteor import Meteor
from StarShipFighterFinal.PowerUP import PowerUp
from StarShipFighterFinal.Gunner import Gunner
from StarShipFighterFinal.GreenLaser import GreenLaser
from StarShipFighterFinal.smallEnemy import smallEnemy
from StarShipFighterFinal.GameOver import * 
import random
import sys
import time 

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 500

'''
The StarShip Fighter will hold most of the logic of the game.
'''

class StarShipFighter():
    
        ''' Displaying the Score
            This fuction will render and display the score on to the screen
            
            Attributes: 
                display_score varible (int) 
            
            Returns:
                str(int)'''
    
        def display_score(self,screen,score):
            score = 'Score : ' + str(score)
            font = pygame.font.SysFont('Buxton Sketch', 30, False, False)
            screen.blit(font.render(score, True, Color(255,255,0)), (20, 10))
        '''
            Checking Collision PowerUP && Checking Collision Gunner
            Attributes:
                fighter - Module will take a 'fighter' object
                powerup - Module will take 'power up' object
                healthbar - Module will take health bar object
                
            Return:
                bool: Returns True if collision occurs within fighter and powerup
        '''
        def checkCollisionPowerup(self,fighter,powerup,healthbar):
            
            if pygame.sprite.collide_rect(fighter, powerup):
                return True
            else:
                return False
      
        def checkCollisionGunner(self,fighter,gunner):
            if pygame.sprite.collide_rect(fighter, gunner):
                return True
            else:
                return False

            '''    Random PowerUp
            Attributes:
                screen - Module will take a 'screen' object
                powerlist - Module will hold the all the powerup sprites  
                allSprites - Module will hold all sprites
                
            Return:
                will randomize a power up object and display it on the screen 
        '''
        def randomPowerUp(self,screen,powerupList,allSprites):
            powerup = PowerUp(250,250,1,1)  
            powerup.draw(screen)
            powerup.randomLocation(screen)
            powerup.move(screen)
            powerupList.add(powerup)
            allSprites.add(powerup)
            
            ''' Random Gunner
            Attributes:
                screen - Module will take a 'screen' object
                powerlist - Module will hold the all the Gunner sprites  
                allSprites - Module will hold all sprites
                
            Return:
                will randomize a Gunner Object object and display it on the screen 
        '''     
        def randomGunner(self,screen,gunnerList,allSprites):          
            gunner = Gunner(250,250,1,1)
            gunner.draw(screen)
            gunner.randomLocation(screen)
            gunner.move(screen)
            gunnerList.add(gunner)
            allSprites.add(gunner)
        '''
            Generate_Meteor
                Attributes: Meteor List- Holds all meteor enemies
                allSprites: Holds all Sprites
                screen_w :Holds the width value of the windows 
                screen-h :Holds the height value of the windows
            
            Return:
                Will Generate random meteor enemies thoughout the screen
        
        '''            
        def generate_meteors(self,meteorlist, allSprites, screen_w, screen_h, num):
            for i in range(num):
                if i % 2 == 0:
                    meteor = Meteor()           
                    meteor.rect.x = random.randrange(screen_w)
                    meteor.rect.y = random.randrange(250)
                    meteorlist.add(meteor)
                    allSprites.add(meteor)
            return meteorlist
        
        '''
            Generate_Enemies
                Attributes: Enemy List- Holds all Enemy Sprites
                allSprites: Holds all Sprites
                screen_w :Holds the width value of the windows 
                screen-h :Holds the height value of the windows
                int(num) : Holds the value of how many enemies will be displayed
            
            Return:
                Will Generate random Enemies thoughout the screen
        
        '''    
        def generate_enemies(self,enemylist, allSprites, screen_w, screen_h, num):
            for i in range(num):
                if i % 2 == 0:
                    enemy = Enemy()            
                    enemy.rect.x = random.randrange(screen_w)
                    enemy.rect.y = random.randrange(300)
                    enemylist.add(enemy)
                    allSprites.add(enemy)
            return allSprites
        

        def GAME(self):
           
            pygame.init()  
            FPS = 30
            fpsClock = pygame.time.Clock()
            
            
            ENEMY_SHOOT = USEREVENT + 1
            ENEMY_SHOOT_SPAWN = 1500
            pygame.time.set_timer(ENEMY_SHOOT, ENEMY_SHOOT_SPAWN)
            
            
            
            

            pygame.display.set_caption('StarShip Fighter')
            
            #-------- Sounds---------#
            laserSound = pygame.mixer.Sound('Sounds/laser5.ogg')
            pygame.mixer.music.load('Sounds/Deepspace_lazers.ogg')
            explosionSound = pygame.mixer.Sound('Sounds/BombExploding.ogg')
            pygame.mixer.music.set_endevent(USEREVENT)
            pygame.mixer.music.play()
           
            #-------------------------------------------------
            
            
            #-------- BackGround--------#
            window_size = (750, 500)
            screen = pygame.display.set_mode(window_size)
            Background = pygame.image.load("images/background.jpg").convert()
            screen.blit(Background,(0,0))
           
            allSprites = pygame.sprite.Group()
            powerUpList = pygame.sprite.Group()
            gunnerList = pygame.sprite.Group()
            fighterList = pygame.sprite.Group()
            enemyList = pygame.sprite.Group()
            bulletList = pygame.sprite.Group()
            enemyBulletList = pygame.sprite.Group()
            meteorList = pygame.sprite.Group()
            blueEnemyList = pygame.sprite.Group()
            #----------------------------------#
         
            #---------Setting up Game----------#
            fighter = Fighter(250,250)
            enemy = Enemy()
            healthbar = HealthBar(screen,250,150)
            powerup = PowerUp(250,250,1,1)
            gunner = Gunner(100,100,1,1)
            healthbar.draw()
            fighter.draw(screen)
            enemy.draw(screen)
            fighterList.add(fighter)
            bullet = GreenLaser()
            enemyList.add(enemy)
            allSprites.add(enemy)
            allSprites.add(fighter)
            
            '''Generate Random Enemies
                    Attributes:
                            Function will take in a list of enemy sprites, All Sprites List
                            int(SCREEN_WIDTH) Holds the value for the width of game
                            int(SCREEN_HEIGHT) Holds the value for the height of game
                            int(num) This holds the value of randomized enemies'''
            
            self.generate_enemies(enemyList, allSprites, SCREEN_WIDTH, SCREEN_HEIGHT, 10)
            self.generate_meteors(meteorList, allSprites, SCREEN_WIDTH, SCREEN_HEIGHT, 20)
           
            
            blueEnemy = smallEnemy(50,100)
            blueEnemy2 = smallEnemy(500,50)
            
#             greeBullet = GreenLaser()
#             greenBullet2 = GreenLaser()
            
            blueEnemyList.add(blueEnemy)
            blueEnemyList.add(blueEnemy2)
            
           
            print("Green Enemies",len(enemyList))
            print(len(blueEnemyList))

            #---------------------------------------------------------------------#
            score = 0
            GAME_OVER = False            
            SINGLE_GUN = True
            GUNNER = False
            AUTOMATIC_GUNNER = True
        
            while True:
                ellapedTime = pygame.time.get_ticks()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                   
                    if event.type == USEREVENT:
                        pygame.mixer.music.play()
                       
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        '''
                    SINGLE_GUN: Fighter will start with a single gunner
                    GUNNER: If fighter obtains Gunner, then SINGLE_GUN will be disable and Active
                            GUNNER (Two Guns)
                        '''
                        if SINGLE_GUN:
                            bullet = Bullet()
                            fighter.createGun(bullet)
                            laserSound.play()
                            allSprites.add(bullet)
                            bulletList.add(bullet)
                        '''
                            Controls the amount of time that Gunner Power up Can be used
                        '''
                        if GUNNER:
                            if pygame.time.get_ticks() < 13000:
                                bullet = Bullet()
                                bullet2 = Bullet()
                                fighter.twoGuns(bullet,bullet2)
                                laserSound.play()
                                allSprites.add(bullet)
                                allSprites.add(bullet2)
                                bulletList.add(bullet)
                                bulletList.add(bullet2)   
                            else:
                                GUNNER = False
                                SINGLE_GUN = True
                                
                    elif   event.type == ENEMY_SHOOT:
                        if AUTOMATIC_GUNNER:
                            greenBullet = GreenLaser()
                            greenBullet.rect.x = blueEnemy.rect.x + 20
                            greenBullet.rect.y = blueEnemy.rect.y + 20
                            blueEnemy.enemyShoot(greenBullet)
                            
                            greenBullet2 = GreenLaser()
                            greenBullet2.rect.x = blueEnemy2.rect.x + 20
                            greenBullet2.rect.y = blueEnemy2.rect.y + 20
                            blueEnemy2.enemyShoot(greenBullet2)
    
                            allSprites.add(greenBullet)
                            enemyBulletList.add(greenBullet)

                            allSprites.add(greenBullet2)
                            enemyBulletList.add(greenBullet2)
                            
                    '''   Movement of the Player
                           Move up : Fighter will be allowed to up in the Y-coordinate 
                           Move Down: Fighter will be allowd to down in the Y-coordinate 
                           Move Right : Fighter will be allowed to up in the X -coordinate 
                           Move Left : Fighter will be allowd to up in the X-coordinate 
                           Move Stop : Player will will main the remaining location given by movement'''
                         
                                     
                    #---------Movement of Players--------------#
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_w:
                            fighter.move_up()
                        if event.key == K_s:
                            fighter.move_down()
                        if event.key == K_a:
                            fighter.move_left(screen)
                        if event.key == K_d:
                            fighter.move_right(screen)
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
                

                ''' Controls when Powerups will apear on screen'''
                if ellapedTime >= 3000 and ellapedTime <= 3030:
                    self.randomPowerUp(screen,powerUpList,allSprites)
                
                if ellapedTime >=4000 and ellapedTime <=4030:
                    self.randomGunner(screen,gunnerList,allSprites)
                        
                #-------------------------------------------------------# 
                ''' Makes the Enemies Move'''
                for enemy in enemyList:
                    enemy.move(fighter,1)
                    if score > 300:
                        enemy.move(fighter, 2)
                     
                    
                
                #-----------Collision Check---------------------------#
                if self.checkCollisionPowerup(fighter,powerup,healthbar):
                    fighter.gainHealth()
                    healthbar.increase_health(25)
                    healthbar.draw()
                    powerUpList.remove(powerup)
                    allSprites.remove(powerup)
                
                if self.checkCollisionGunner(fighter, gunner):
                    gunnerList.remove(gunner)
                    allSprites.remove(gunner)
                    GUNNER = True
                #---------------------------------------------------------#   
                
                if GUNNER: 
                    SINGLE_GUN = False
                
                ''' Enemy getting hit Logic
                        For every bullet that is colliable with enemey. 
                        Health will be decreased. 
                        after health is less than zero, sprites will be removed'''
                    
                    
                for bullet in bulletList:    
                    blockedBlueEnemy = pygame.sprite.spritecollide(bullet, blueEnemyList,False)  
                    
                    if blockedBlueEnemy:
                        bulletList.remove(bullet)
                        allSprites.remove(bullet)
                        blueEnemy.updateHealth()
                        
                        print(blueEnemy.updateHealth())
                        print('Collided')
                        
                        if blueEnemy.getHealth() <= 0:
                            bullet
                            allSprites.remove(blueEnemy)
                            blueEnemyList.remove(blueEnemy)

                #----------Enemy Getting Hit------------#
                for bullet in bulletList:
                    blockEnemyList = pygame.sprite.spritecollide(bullet, enemyList, False)
                    blockMeteorList = pygame.sprite.spritecollide(bullet,meteorList, False)
                           
                    for meteor in blockMeteorList:
                        bulletList.remove(bullet)
                        allSprites.remove(bullet)
                        meteor.updateMeteorHealth()
                        
                        if meteor.getHealth() <= 0: 
                            bulletList.remove(bullet)
                            meteorList.remove(meteor)
                            allSprites.remove(meteor)
                            allSprites.remove(bullet)
                            score +=75                         
                    
                    for enemy in blockEnemyList:
                        explosion = SmallExplosion(enemy)
                        explosion.draw(screen)
                        bulletList.remove(bullet)
                        allSprites.remove(bullet)
                        enemy.updateHealth()
            
                        if enemy.getHealth() <= 0:
                            explosionSound.play()
                            bigExplosion = BigExplosion(enemy)
                            bigExplosion.draw(screen)  
                            enemyList.remove(enemy)
                            allSprites.remove(enemy)
                            score = score + 150
                            print('Score',score)
                            
       
                for bullet in enemyBulletList:
                    fighterDown = pygame.sprite.spritecollide(bullet, fighterList,False)
                    
                    for fighter in fighterDown:
                        healthbar.draw()
                        fighter.updateHealth()
                        healthbar.decrease_health(10)
                        enemyBulletList.remove(bullet)
                        allSprites.remove(bullet)
                        
                        if fighter.getHealth() <= 0:
                            fighterList.remove(fighter)
                            allSprites.remove(fighter)
                            enemyList.remove(enemy)
                            GAME_OVER = True 
                  
                #---------------------------------------------------#
                '''
                    Game Logic
                        If any of the enemis collide with fighter
                        fighter will loose health
                        healthbar will adjust to the health of fighter
                '''
                for enemy in enemyList: 
                    blockedFighter = pygame.sprite.spritecollide(enemy, fighterList, False)
                    
                    for fighter in blockedFighter: 
                        explosion = SmallExplosion(fighter)
                        explosion.draw(screen)
                        healthbar.draw()
                        fighter.updateHealth()
                        healthbar.decrease_health(10)
                       
                
                        if fighter.getHealth() <= 0:
                            fighterList.remove(fighter)
                            allSprites.remove(fighter)
                            enemyList.remove(enemy)
                            GAME_OVER = True
                            
                            
                            
                if GAME_OVER: 
                    GameOver().Over()
                
                ''' Movement for all Sprites
                        Powerups - powerup will be floating around the screen
                        Gunner - gunner will be floating around the screen
                '''    
                for powerup in powerUpList:
                    powerup.move(screen)  
                    
                for gunner in gunnerList:
                    gunner.move(screen)      
                
                '''
                    Purpose:
                        Fighter must destroy all enemies and meteor in order to beat the game
                        
                        Return:
                            This check if there is any sprites left in the list of enemies/meteors
                '''
                if len(enemyList) == 0 and len(meteorList) ==0 and len(blueEnemyList) == 0:
                    gameover = GameOver()
                    gameover.Over()
                
                '''
                    Update The Game
                        Must Blit the screen
                        update all necessary Sprites
                        Display Score at all time 
                '''        
                screen.blit(Background,(0,0)) 
                fighter.update()
                healthbar.draw()
                
#                 blueEnemy.draw(screen)
#                 blueEnemy2.draw(screen)
#                 enemyBulletList.update()
                gunnerList.update()
                powerUpList.update()
                allSprites.update()            
                allSprites.draw(screen)
                self.display_score(screen, score)
                pygame.display.flip()

                pygame.display.update()      
                fpsClock.tick(FPS)    
  
# game = StarShipFighter()
# game.GAME()