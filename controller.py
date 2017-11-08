# the controller takes a keyboard or mouse event from the main game loop and performs
# the corresponding action
# the controller controls the player's ship and the main menu
import pygame
import ship

class Controller:

	def __init__controller(self):
		self.player = ship.AdvancedShip()

	def setShipPosition():
		# get mouse position on the screen
		mousePos = pygame.mouse.get_pos()


	# returns True or False, True if game is to exit, False if not
	def handleEvent(self):
		for event in pygame.event.get():
			# all handlers for kayboard/mouse events
			if not hasattr(event, "key"): continue
			if event.key == pygame.K_ESCAPE: return True
		return False