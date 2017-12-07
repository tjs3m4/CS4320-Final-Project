# the class responsible for managing the screen and drawing to it
import pygame
# from pygame.locals import *
import gameState
# import os

class GraphicsManager:
	def __init__(self, screenSize, bullets, ships, weapons, mMenu, pMenu):
		self.screenSize = screenSize
		self.screen = pygame.display.set_mode(self.screenSize, pygame.DOUBLEBUF)
		pygame.display.set_caption("") # sets the text on the top of the window
		self.renderSurface = pygame.Surface(screenSize) # draw any object to this surface, then this surface to the screen at end of draw loop. This helps prevent flickering
		self.bullets = bullets
		self.ships = ships
		self.weapons = weapons
		self.animationTimer = 5 # how many iterations of the game loop before the animation in played
		self.tickCount = 0 # the game loop counter 
		
		self.bkgd = pygame.image.load("images/background.png").convert()
		# bkgd = pygame.transform.scale(bkgd, (1280, 800))
		self.mMenu = mMenu
		self.pMenu = pMenu

		self.greyTone = pygame.Surface(screenSize) # for greying out the game to better indicate that the game is paused
		pygame.draw.rect(self.greyTone, (0, 0, 0), (0, 0, screenSize[0], screenSize[1]) , 0)
		self.greyTone.set_alpha(155)
		self.player = ships[0]

	def updateGraphics(self, state):
		self.tickCount += 1;
		self.renderSurface.fill((0,0,0)) # clear the render surface

		if state == gameState.GameState.GAME_EXIT: # don't draw graphics on game quit event
			return

		if state == gameState.GameState.MAIN_MENU: # MAIN_MENU
			self.displayMainMenu()

		else:
			self.renderSurface.blit(self.bkgd,(0,0))# draw background image
			if (self.tickCount >= self.animationTimer):
				self.player.animate()
			self.renderSurface.blit(self.player.texture, self.player.sprite) # draw player

			for enemy in self.ships:
				if (self.tickCount >= self.animationTimer):
					enemy.animate()
				self.renderSurface.blit(enemy.texture, enemy.sprite) # draw all enemy ships

			for weapon in self.weapons:
				self.renderSurface.blit(weapon.texture, weapon.sprite) # draw weapons

			if (self.tickCount >= self.animationTimer): # reset count for animation
				self.tickCount = 0

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

