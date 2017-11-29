class Bullet:
	def __init__(self, x, y, velX, velY, image):
		self.velX = 0 # speed of ship in the X direction, used to update position on screen every iteration of game loop
		self.velY = 0 # speed of the ship in the Y direction
		self.angle = 0 # an angle, represents the direction the ship is facing
		self.damage = 0 # value representing the amount of damage the bullet will do
		self.texture = 0 # image represtenting the bullet
		self.sprite = 0 # the rectangle the bullet is drawn to