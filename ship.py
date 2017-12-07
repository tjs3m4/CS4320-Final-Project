import weapon
import pygame
from math import degrees
from math import atan2

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