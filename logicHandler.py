import gameState
from random import randint
import ship
import weapon
import pygame
import math

# class used to keep track of and update the game logic as the game plays
class LogicHandler():

	def __init__(self, screenSize, bullets, ships, weapons, col_ships):
		self.bullets = bullets
		self.ships = ships
		self.weapons = weapons
		self.screenSize = screenSize
		self.spawnTick = 300 # how many iterations of the game loop before we spawn a new enemy ship. higher value = slower ship spawning
		self.tickCount = 0 # the game loop counter to see if it is time to spawn an enemy
		self.tickCount1 = 0 # the game loop counter to see if it is time to spawn an enemy
		self.tickCount2 = 0 # the game loop counter to see if it is time to spawn a bullet

		self.fireRate = 3

		self.enemyShipImage = pygame.image.load("images/enemy_plane.png")
		self.enemyAnimation = pygame.image.load("images/enemy_planefly.png")
		self.weaponImage = pygame.image.load("images/weapon_supply.png")
		self.bulletImage = pygame.image.load("images/bullet.png")
		self.bulletAnimation = pygame.image.load("images/bullet.png")
		self.player = ships.pop(0) # get player ship
		self.col_ships = col_ships # a list of (x,y) coordinates to indicate where a collision occuured

	# called from the main game loop
	# calls updateBullets and updateShips
	def updateGameLogic(self, state):
		self.tickCount += 1
		self.tickCount1 += 0.25
		self.tickCount2 += self.fireRate

		if state == gameState.GameState.GAME_RESET: # play button was hit.
			state = self.resetGame()

		if state == gameState.GameState.PLAYING: # PLAYING
			self.updateShips()
			self.updateBullets()
			self.updateWeapon()

			if self.tickCount >= self.spawnTick:
				self.tickCount = 0
				self.spawnEnemyShip()

			if self.tickCount2 >= self.spawnTick:
				self.tickCount2 = 0
				self.spawnBullet()

			if self.tickCount1 >= self.spawnTick:
				self.tickCount1 = 0
				self.spawnWeapon()

			self.collisionDetect()
			if self.checkGameOver() == True:
				state = gameState.GameState.GAME_OVER

		return state


	def resetGame(self):
		self.player.resetShip() # reset the position and health of the player
		self.ships.clear() # clear ship list
		self.col_ships.clear() # clear collisions
		self.bullets.clear() # clear bullets
		self.weapons.clear()
		self.fireRate = 3
		return gameState.GameState.PLAYING


	def checkGameOver(self):
		if self.player.health <= 0:
			return True
		else:
			return False


	def spawnEnemyShip(self):
		side = randint(0,3)
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

	def spawnWeapon(self):
		locX = randint(100, 950)
		locY = 0
		self.weapons.append(weapon.Weapon(self.weaponImage, locX, locY, 1))

	def spawnBullet(self):
		locX = self.player.x
		locY = self.player.y
		self.bullets.append(ship.Bullet(self.bulletImage, self.bulletAnimation, locX, locY, 1, self.player))

	def updateWeapon(self):
		for weapon in self.weapons:
			weapon.move()

	# updates the position of all bullets on the screen
	def updateBullets(self):
		for bullet in self.bullets:
			bullet.move()

	# updates the position of all ships on the screen and checks for collision with a bullet or another ship
	def updateShips(self):
		self.player.move()
		self.player.rotate()
		for ship in self.ships:
			ship.rotate()
			ship.move()
		self.checkPlayerBoundary();

	def collisionDetect(self):
		for ship in self.ships: # check if an enemy ship collides with the player
			if self.player.hitbox.colliderect(ship.hitbox):
				# add collision to list
				self.col_ships.append(ship.hitbox.center)
				# destroy ship
				self.ships.remove(ship)
				# decrement player health
				self.player.health -= 1

		for bullet in self.bullets: # check if a bullet collides with an enemy ship
			for ship in self.ships:
				if ship.hitbox.colliderect(bullet.hitbox):
					# collision detected
					self.col_ships.append(ship.hitbox.center)
					self.ships.remove(ship)

		# weapon supply
		for weapon in self.weapons: # check collision with weapon supply
			if self.player.hitbox.colliderect(weapon.sprite):
				self.fireRate *= 1.2
				self.weapons.remove(weapon)



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