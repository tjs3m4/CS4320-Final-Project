import gameState

# class used to keep track of and update the game logic as the game plays
class LogicHandler():

	def __init__(self, screenSize, bullets, ships):
		self.bullets = bullets
		self.ships = ships
		self.screenSize = screenSize

	# called from the main game loop
	# calls updateBullets and updateShips
	def updateGameLogic(self, state):
		if state == gameState.GameState.PLAYING: # PLAYING
			self.updateShips()
			self.updateBullets()

	# updates the position of all bullets on the screen
	def updateBullets(self):

		return

	# updates the position of all ships on the screen and checks for collision with a bullet or another ship
	def updateShips(self):
		for ship in self.ships:
			ship.rotate()
			ship.move()

		# player ship is the first ship in the list, and the only ship to be affected by screen borders		
		# check position relative to screen borders
		# setting the ship's position is necessary, as it has the possibility of getting stuck if not set and the absolute value of the constant that changes velocity is < 1
		if  self.ships[0].x <= 0: # hit left of screen
			self.ships[0].x = 0
			self.ships[0].velX *= -0.66

		elif self.ships[0].x >= self.screenSize[0]: # hit right of screen
			self.ships[0].x = self.screenSize[0]
			self.ships[0].velX *= -0.66


		elif self.ships[0].y <= 0: # hit top of screen
			self.ships[0].y = 0
			self.ships[0].velY *= -0.66

		elif self.ships[0].y >= self.screenSize[1]: # hit bottom of screen
			self.ships[0].y = self.screenSize[1]
			self.ships[0].velY *= -0.66
