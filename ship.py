import weapon
import pygame

# Base class for all ships
class Ship:

	def __init__(self, image, x , y, health):
		self.x = x # x part of coordinate on screen
		self.y = y # y part of coordinate on screen
		self.velX = 0 # speed of ship in the X direction, used to update position on screen every iteration of game loop
		self.velY = 0 # speed of the ship in the Y direction
		self.angle = 0 # an angle, represents the direction the ship is facing
		self.health = 0 # value representing the amount of health the ship has remaining
		self.masterTexture = image # the master copy of the image, never assign anything to this
		self.texture = self.masterTexture # manipulated image used to draw to the screen
		self.sprite = image.get_rect(center = (self.x, self.y)) # the rectangle which the image is drawn onto

	# accelerates the ship by increasing its velocity
	def accelerate(self):
		pos = pygame.mouse.get_pos()
		self.velX += ((pos[0] - self.x) * 0.5) / 8300
		self.velY += ((pos[1] - self.y) * 0.5) / 8300
		# TODO: draw burner image

	# moves the ship according to its angle and velocity
	def move(self):
		self.x += self.velY
		self.y += self.velX
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
	
	def __init__(self, image, x , y, health):
		self.weapon = weapon.Weapon()
		super(AdvancedShip, self).__init__(image, x, y, health)

	def fire(self):
		# TODO
		# create a new bullet at the front of the ship

		return

class EnemyShip(Ship):

	def __init__(self, image, x , y, health):
		# super(Ship, self).__init__(self, image, x , y, health)
		self.x = 10 # x part of coordinate on screen
		self.y = 10 # y part of coordinate on screen
		self.velX = 10 # speed of ship in the X direction, used to update position on screen every iteration of game loop
		self.velY = 10 # speed of the ship in the Y direction
		self.angle = 10 # an angle, represents the direction the ship is facing
		self.health = 1 # value representing the amount of health the ship has remaining
		self.masterTexture = image # the master copy of the image, never assign anything to this
		self.texture = self.masterTexture # manipulated image used to draw to the screen
		self.sprite = image.get_rect(center = (self.x, self.y)) # the rectangle which the image is drawn onto
		enemyShipImage = pygame.image.load("images/p_ship-red.png")		
		self.enemys = self.AdvancedEnemyShip(enemyShipImage, screenSize[0] / 3, screenSize[1] / 3, 1)

	# 	# TODO: draw burner image

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


	# other funcitons for enemyShip AI
	# overrides base ship accelerate()
	def accelerate(self):
		pos = pygame.mouse.get_pos()
		self.velX += ((pos[0] - self.x) * 0.5) / 80000
		self.velY += ((pos[1] - self.y) * 0.5) / 80000
		

class AdvancedEnemyShip(AdvancedShip):
	def __init__(self, image, x , y, health):
		super(AdvancedEnemyShip, self).__init__(self, image, x, y, health)

	# other functions for AdvancedShip AI