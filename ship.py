import weapon
import pygame
import math
from math import degrees
from math import atan2 
from math import sin
from math import cos



# Base class for all ships
class Ship:

	def __init__(self, image, animation, x , y, health):
		self.x = x # x part of coordinate on screen
		self.y = y # y part of coordinate on screen
		self.velX = 0 # speed of ship in the X direction, used to update position on screen every iteration of game loop
		self.velY = 0 # speed of the ship in the Y direction
		self.angle = 0 # an angle, represents the direction the ship is facing
		self.health = 0 # value representing the amount of health the ship has remaining
		self.masterTexture = image # the master copy of the image, used to refresh the texture so that it doesn't get distorted
		self.texture = self.masterTexture # manipulated image used to draw to the screen
		self.sprite = image.get_rect(center = (self.x, self.y)) # the rectangle which the image is drawn onto

		self.animation2 = image
		self.animation = animation
		self.animation_state = False # False: image is off, True: image is on

	def animate(self):
		if self.animation_state == False:
			self.animation_state = True
			self.masterTexture = self.animation
		else:
			self.animation_state = False
			self.masterTexture = self.animation2


	# accelerates the ship by increasing its velocity
	def accelerate(self):
		pos = pygame.mouse.get_pos()
		self.velX += ((pos[0] - self.x) * 0.5) / 8300
		self.velY += ((pos[1] - self.y) * 0.5) / 8300
		# TODO: draw burner image
    
	# moves the ship according to its angle and velocity
	def move(self):
		self.x += self.velX
		self.y += self.velY
		self.sprite = self.texture.get_rect(center=(self.x, self.y))

	# when we want to rotate the ship, we use the pygame.transform.rotate() funciton.
	# it creates a new image from a given image, therefore, we give it the masterTexture and assign the result to the texture
		# this is to avoid warping the image too much by making a copy of a copy of a copy....
	# additionally, we have to reset the center, because the dimensions of the texture are changed by the rotation
	def rotate(self):
		self.texture = pygame.transform.rotate(self.masterTexture, self.angle)
		self.sprite = self.texture.get_rect(center=self.sprite.center)

# same functionality as a Ship, but has a weapon and is capable of firing
# the player and boss ships will be of this type
class AdvancedShip(Ship):
	
	def __init__(self, image, animation, x , y, health):
		self.weapon = weapon.Weapon(image, x, y, health)
		super(AdvancedShip, self).__init__(image, animation, x, y, health)

	def fire(self):
		# TODO
		# create a new bullet at the front of the ship

		return

class EnemyShip(Ship):

	def __init__(self, image, animation, x , y, health, playerShip):
		super(EnemyShip, self).__init__(image, animation, x , y, health)
		self.playerShip = playerShip

	# other funcitons for enemyShip AI
	# overrides base ship accelerate()
	def accelerate(self):
		playerX = self.playerShip.x
		playerY = self.playerShip.y		
		self.velX += ((playerX - self.x) * 0.2) / 8300
		self.velY += ((playerY - self.y) * 0.2) / 8300

	def move(self):
		self.rotate() # face player ship
		self.accelerate() # move towards player ship
		self.x += self.velX
		self.y += self.velY
		self.sprite = self.texture.get_rect(center=(self.x, self.y))

	def rotate(self):
		playerX = self.playerShip.x
		playerY = self.playerShip.y
		self.angle = (-1 * degrees(atan2(playerY - self.y, playerX - self.x))) - 90
		self.texture = pygame.transform.rotate(self.masterTexture, self.angle)
		self.sprite = self.texture.get_rect(center=self.sprite.center)

class AdvancedEnemyShip(AdvancedShip):
	def __init__(self, image, x , y, health):
		super(AdvancedShip, self).__init__(self, image, x, y, health)

	# other functions for AdvancedShip AI

class Bullet(Ship):

	def __init__(self, image, animation, x , y, health, playerShip):
		super(Bullet, self).__init__(image, animation, x , y, health)
		self.playerShip = playerShip

	# other funcitons for enemyShip AI
	# overrides base ship accelerate()
	def move(self):
			if (self.x >= 0.9 * self.playerShip.x) and (self.x <= 1.1 * self.playerShip.x) and (self.y >= 0.9 * self.playerShip.y) and (self.y <= 1.1 * self.playerShip.y):
				pos = pygame.mouse.get_pos()
				self.angle = degrees(atan2(400 - pos[1], pos[0] - 512)) - 90  #self.playerShip.angle
				self.velX = (pos[0] - 512) / 50
				self.velY = (pos[1] - 400) / 50
				self.x += (pos[0] - 512) / 10
				self.y += (pos[1] - 400) / 10
				self.texture = pygame.transform.rotate(self.masterTexture, self.angle)
				self.sprite = self.texture.get_rect(center=(self.x, self.y))
			elif (self.x != self.playerShip.x) and (self.y != self.playerShip.y):
				self.x += 2 * self.velX
				self.y += 2 * self.velY
				self.texture = pygame.transform.rotate(self.masterTexture, self.angle)
				self.sprite = self.texture.get_rect(center=(self.x, self.y))



