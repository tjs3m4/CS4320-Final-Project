import gameState
from random import randint
import ship
import pygame
import math

# class used to keep track of and update the game logic as the game plays
class LogicHandler():

        def __init__(self, screenSize, bullets, ships,col_ships):
                self.bullets = bullets
                self.ships = ships
                self.screenSize = screenSize
                self.spawnTick = 300 # how many iterations of the game loop before we spawn a new enemy ship. higher value = slower ship spawning
                self.tickCount = 0 # the game loop counter to see if it is time to spawn an enemy
                self.enemyShipImage = pygame.image.load("images/enemy_plane.png")
                self.enemyAnimation = pygame.image.load("images/enemy_planefly.png")
                self.player = ships.pop(0) # get player ship
                self.col_ships = col_ships

        # called from the main game loop
        # calls updateBullets and updateShips
        def updateGameLogic(self, state):
                self.tickCount += 1
                if state == gameState.GameState.PLAYING: # PLAYING
                        self.updateShips()
                        self.updateBullets()

                        if self.tickCount >= self.spawnTick:
                                self.tickCount = 0
                                self.spawnEnemyShip()

        def spawnEnemyShip(self):
                side = randint(0,3)
                num = 0
                if side == 0: # left side
                        locX = randint(-250, -50)
                        locY = randint(-200, self.screenSize[1] + 200) # (-200 to 1000)
                        self.ships.append(ship.EnemyShip(self.enemyShipImage, self.enemyAnimation, locX, locY, 1, self.player))

                elif side == 1: # bottom side
                        locX = randint(-200, self.screenSize[0] + 200) # (-200 to 1224)
                        locY = randint(self.screenSize[1] + 50, self.screenSize[1] + 250) # (850 to 1050)
                        self.ships.append(ship.EnemyShip(self.enemyShipImage, self.enemyAnimation, locX, locY, 1, self.player))

                elif side == 2: # right side
                        locX = randint(self.screenSize[0] + 50, self.screenSize[0] + 250) # (1074, 1274)
                        locY = randint(-200, self.screenSize[1] + 200) # (-200, 1000)
                        self.ships.append(ship.EnemyShip(self.enemyShipImage, self.enemyAnimation, locX, locY, 1, self.player))

                elif side == 3: # top side
                        locX = randint(-200, self.screenSize[0] + 200) # (-200, 1224)
                        locY = randint(-250, -50) # (-250, -50)
                        self.ships.append(ship.EnemyShip(self.enemyShipImage, self.enemyAnimation, locX, locY, 1, self.player))

                for each in self.ships:
                        distance = math.sqrt(\
                                math.pow((self.player.x-each.x),2)+\
                                math.pow((self.player.y-each.y),2)\
                                )
                        if distance <=(self.player.rect.width+each.rect.width):
                                self.col_ships.append(each)
                                self.player.velX = -self.player.velX
                                self.player.velY = -self.player.velY
                                print("-1s")


        #def collideCheck(self):
         #       for each in self.ships:
          #              distance = math.sqrt(\
           #                     math.pow((self.player.rect.center[0]-each.rect.center[0]),2)+\
            #                    math.pow((self.player.rect.center[1]-each.rect.center[1]),2)\
             #                   )
              #          if distance <=(self.player.rect.width+each.rect.width)/2:
               #                 self.col_ships.append(enemy)
                #                self.player.velX = -self.player.velX
                 #               self.player.velY = -self.player.velY
                  #              print("XXX")
                
        
        # updates the position of all bullets on the screen
        def updateBullets(self):

                return

        # updates the position of all ships on the screen and checks for collision with a bullet or another ship
        def updateShips(self):
                self.player.move()
                self.player.rotate()
                for ship in self.ships:
                        ship.rotate()
                        ship.move()

                self.checkPlayerBoundary();

        def checkPlayerBoundary(self):
                # player ship is the first ship in the list, and the only ship to be affected by screen borders         
                # check position relative to screen borders
                # setting the ship's position is necessary, as it has the possibility of getting stuck if not set and the absolute value of the constant that changes velocity is < 1
                if  self.player.x <= 0: # hit left of screen
                        self.player.x = 0
                        self.player.velX *= -0.66

                elif self.player.x >= self.screenSize[0]: # hit right of screen
                        self.player.x = self.screenSize[0]
                        self.player.velX *= -0.66

                elif self.player.y <= 0: # hit top of screen
                        self.player.y = 0
                        self.player.velY *= -0.66

                elif self.player.y >= self.screenSize[1]: # hit bottom of screen
                        self.player.y = self.screenSize[1]
                        self.player.velY *= -0.66
