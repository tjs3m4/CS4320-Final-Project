import ship

class Bullet:
	def __init__(self, image, x, y, health, playerShip):
		self.x = x # x part of coordinate on screen
		self.y = y # y part of coordinate on screen
		self.health = 0
		self.playerShip = ship.playerShip
		self.masterTexture = image # the master copy of the image, used to refresh the texture so that it doesn't get distorted
		self.texture = self.masterTexture # manipulated image used to draw to the screen
		self.sprite = image.get_rect(center = (self.x, self.y)) # the rectangle the bullet is drawn to

	def move(self):
		#playervelX = self.playerShip.velx
		#playervelY = self.playerShip.vely	
		self.x += 0
		self.y += 10
		self.sprite = self.texture.get_rect(center=(self.x, self.y))
