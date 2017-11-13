import bullet

class Weapon():
	def __init__(self):
		# self.bullet = bullet.Bullet() # the bullet type that is fired. These will be copy-created every time the weapon is fired
		self.sprite = 0 # image representing the weapon on the screen