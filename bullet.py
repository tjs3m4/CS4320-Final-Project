class Bullet:
	def __init__(self):
		self.x # x part of coordinate on screen
		self.y # y part of coordinate on screen
		self.velocity # speed of bullet, used to update position on screen every iteration of game loop
		self.angle # an angle, represents the direction the bullet is traveling
		self.damage # value representing the amount of damage the bullet will do
		self.sprite # the image representation of the bullet on the screen