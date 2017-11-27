# the class responsible for managing the screen and drawing to it
import pygame
import gameState

class GraphicsManager:
	def __init__(self, screenSize, bullets, ships, mMenu, pMenu):
		self.screenSize = screenSize
		self.screen = pygame.display.set_mode(self.screenSize, pygame.DOUBLEBUF)
		pygame.display.set_caption("") # sets the text on the top of the window
		self.bullets = bullets
		self.ships = ships

		self.mMenu = mMenu
		self.pMenu = pMenu

		self.greyTone = pygame.Surface(screenSize)
		pygame.draw.rect(self.greyTone, (0, 0, 0), (0, 0, screenSize[0], screenSize[1]) , 0)
		self.greyTone.set_alpha(155)

	def updateGraphics(self, state):
		if state == gameState.GameState.GAME_EXIT: # don't draw graphics on game quit event
			return

		self.screen.fill((0,0,0))

		if state == gameState.GameState.MAIN_MENU: # MAIN_MENU
			self.displayMainMenu()

		else:
			for ship in self.ships:
				self.screen.blit(ship.texture, ship.sprite)

			if state == gameState.GameState.PAUSE_MENU: # PAUSE_MENU
				self.screen.blit(self.greyTone, (0, 0)) # draw grey undertone to dull game objects
				self.displayPauseMenu()

		pygame.display.flip() # draw to the screen

	def displayMainMenu(self):
		# tuples are read only, have to read size of screen into another variable
		for key, btn in self.mMenu.items(): # loop to iterate over dictionary
			self.screen.blit(btn.activeTexture, btn.sprite)
		return

	def displayPauseMenu(self):
		for key, btn in self.pMenu.items(): # loop to iterate over dictionary
			self.screen.blit(btn.activeTexture, btn.sprite)
		return

