# the controller takes a keyboard or mouse event from the main game loop and performs
# the corresponding action
# the controller controls the player's ship and the main menu
import pygame
import ship
from math import degrees
from math import atan2

class Controller:
	def __init__(self):
		playerShipImage = pygame.image.load("images/p_ship.png")
		self.player = ship.AdvancedShip(playerShipImage, 400, 400, 3)

	# gets mouse position on the screen and
	# determines angle of the mouse relative to the screen center
	# then sets the angle of the ship equal to the computed angle
	def setShipAngle(self):
		mousePos = pygame.mouse.get_pos()
		# atan2 is used when the signs of both x and y are known
		self.player.angle = (-1 * degrees(atan2(mousePos[1] - self.player.y, mousePos[0] - self.player.x))) - 90

	# adds to the player's velocity

	# returns True or False, True if game is to exit, False if not
	def handleInputs(self, state):
		# to be sure the ship angle is constantly looking at the mouse cursor
		self.setShipAngle()
		
		(m1,m2,m3) = pygame.mouse.get_pressed() # right mouse button = m3, left mouse button = m1, middle mouse = m2
		if m3 == True: # if the right mouse button is held down
			self.player.accelerate()

		if m1 == True: # if the left mouse button is held down
			self.player.fire()

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE: return True # access pause menu or resume game depending on state of the game

		return False