# basic small enemy ships will be of this type
class Ship:

	def __init__(self):
		self.x # x part of coordinate on screen
		self.y # y part of coordinate on screen
		self.velocity # speed of ship, used to update position on screen every iteration of game loop
		self.angle # an angle, represents the direction the ship is facing
		self.health # value representing the amount of health the ship has remaining
		self.sprite # the image representation of the ship on the screen

	# rotates the ship clockwise (positive argument) or counter-clockwise (negative argument)
	def rotate(self, direction):
		self.angle += direction

	# accelerates the ship by increasing its velocity
	def accelerate(self):
		return


	# moves the ship according to its angle and velocity
	def move(self):
		return

# same functionality as a Ship, but has a weapon and is capable of firing
# the player and boss ships will be of this type
class AdvancedShip(Ship):
	
	def __init__(self):
		self.weapon

	def fire():
		return