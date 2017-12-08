import bullet

class Weapon():
	def __init__(self, image, x , y, health):
		self.x = x # x part of coordinate on screen
		self.y = y # y part of coordinate on screen
		self.health = 0 # value representing the amount of health the ship has remaining
		self.masterTexture = image # the master copy of the image, used to refresh the texture so that it doesn't get distorted
		self.texture = self.masterTexture # manipulated image used to draw to the screen
		self.sprite = image.get_rect(center = (self.x, self.y)) # the rectangle which the image is drawn onto

	def move(self):
		self.x += 0
		self.y += 3
		self.sprite = self.texture.get_rect(center=(self.x, self.y))
