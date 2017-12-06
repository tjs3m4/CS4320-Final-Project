# the class responsible for managing the screen and drawing to it
import pygame
import gameState

class GraphicsManager:
	def __init__(self, screenSize, bullets, ships, mMenu, pMenu):
		self.screenSize = screenSize
		self.screen = pygame.display.set_mode(self.screenSize, pygame.DOUBLEBUF)
		pygame.display.set_caption("") # sets the text on the top of the window
		self.renderSurface = pygame.Surface(screenSize) # draw any object to this surface, then this surface to the screen at end of draw loop. This helps prevent flickering
		self.bullets = bullets
		self.ships = ships

		self.mMenu = mMenu
		self.pMenu = pMenu

		self.greyTone = pygame.Surface(screenSize) # for greying out the game to better indicate that the game is paused
		pygame.draw.rect(self.greyTone, (0, 0, 0), (0, 0, screenSize[0], screenSize[1]) , 0)
		self.greyTone.set_alpha(155)
		self.player = ships[0]

	def updateGraphics(self, state):
		self.renderSurface.fill((0,0,0)) # clear the render surface

		if state == gameState.GameState.GAME_EXIT: # don't draw graphics on game quit event
			return

		if state == gameState.GameState.MAIN_MENU: # MAIN_MENU
			self.displayMainMenu()

		else:
			self.renderSurface.blit(self.player.texture, self.player.sprite) # draw player
			for ship in self.ships:
				self.renderSurface.blit(ship.texture, ship.sprite)

			if state == gameState.GameState.PAUSE_MENU: # PAUSE_MENU
				self.renderSurface.blit(self.greyTone, (0, 0)) # draw grey undertone to dull game objects
				self.displayPauseMenu()

		self.screen.blit(self.renderSurface, (0, 0)) # draw surface to the screen
		pygame.display.flip() # display newly rendered screen

	def displayMainMenu(self):
		# tuples are read only, have to read size of screen into another variable
		for key, btn in self.mMenu.items(): # loop to iterate over dictionary
			self.renderSurface.blit(btn.activeTexture, btn.sprite)
		return

	def displayPauseMenu(self):
		for key, btn in self.pMenu.items(): # loop to iterate over dictionary
			self.renderSurface.blit(btn.activeTexture, btn.sprite)
		return

