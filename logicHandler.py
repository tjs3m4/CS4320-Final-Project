# class used to keep track of and update the game logic as the game plays
class LogicHandler():

	def __init__(self, bullets, ships):
		self.bullets = bullets
		self.ships = ships

	# called from the main game loop
	# calls updateBullets and updateShips
	def updateGameLogic(self):
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