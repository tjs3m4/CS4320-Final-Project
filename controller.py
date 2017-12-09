# the controller takes a keyboard or mouse event from the main game loop and performs
# the corresponding action
# the controller controls the player's ship and the main menu
import pygame
import ship
from math import degrees
from math import atan2
import gameState

class Controller:
	def __init__(self, screenSize, mMenu, pMenu):
		playerShipImage = pygame.image.load("images/myplane2_1.png")
		playerAnimation = pygame.image.load("images/myplane2_1.png")
		self.player = ship.AdvancedShip(playerShipImage, playerAnimation, screenSize[0] / 2, screenSize[1] / 2, 3)

		self.mMenu = mMenu
		self.pMenu = pMenu

	# returns True or False, True if game is to exit, False if not
	def handleInputs(self, state):
		# to be sure the ship angle is constantly looking at the mouse cursor
		if state == gameState.GameState.PLAYING:
			self.setShipAngle()
		# or to indicate the menu button that is being hovered over by the mouse
		elif state != gameState.GameState.GAME_EXIT:
			self.setActiveMenuBtn(state)

		# handle for mouse buttons being held down
		# ------------------------------------------
		(m1,m2,m3) = pygame.mouse.get_pressed() # right mouse button = m3, left mouse button = m1, middle mouse = m2

		if m3 == True and state == gameState.GameState.PLAYING: # if the right mouse button is held down
			self.player.accelerate()

		if m1 == True and state == gameState.GameState.PLAYING: # if the left mouse button is held down
			self.player.fire()
		# ------------------------------------------

		# handle for key press or single mouse click
		# ------------------------------------------
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE: # access pause menu or resume game depending on state of the game
					if state == gameState.GameState.PLAYING:
						state = gameState.GameState.PAUSE_MENU
					elif state == gameState.GameState.PAUSE_MENU:
						state = gameState.GameState.PLAYING

			# single mouse click is only relevent inside the menus
			if state == gameState.GameState.PAUSE_MENU or state == gameState.GameState.MAIN_MENU:
				if event.type == pygame.MOUSEBUTTONDOWN: # handle single mouse click
					state = self.checkMenuBtnClick(state)
		# ------------------------------------------

		return state


	# gets mouse position on the screen and
	# determines angle of the mouse relative to the screen center
	# then sets the angle of the ship equal to the computed angle
	def setShipAngle(self):
		mousePos = pygame.mouse.get_pos()
		# atan2 is used when the signs of both x and y are known
		self.player.angle = (-1 * degrees(atan2(mousePos[1] - self.player.y, mousePos[0] - self.player.x))) - 90

	def setActiveMenuBtn(self, state):
		mousePos = pygame.mouse.get_pos()
		if state == gameState.GameState.PAUSE_MENU:
			for key, btn in self.pMenu.items(): # loop to iterate over dictionary
				if btn.sprite.collidepoint(mousePos):
					btn.hover()
				else:
					btn.setInactive()
		elif state == gameState.GameState.MAIN_MENU:			
			for key, btn in self.mMenu.items(): # loop to iterate over dictionary
				if btn.sprite.collidepoint(mousePos):
					btn.hover()
				else:
					btn.setInactive()

	def checkMenuBtnClick(self, state):
		mousePos = pygame.mouse.get_pos()
		if state == gameState.GameState.PAUSE_MENU:
			for key, btn in self.pMenu.items(): # loop to iterate over dictionary
				if btn.sprite.collidepoint(mousePos):
					state = btn.onClick(state)

		elif state == gameState.GameState.MAIN_MENU:
			for key, btn in self.mMenu.items(): # loop to iterate over dictionary
				if btn.sprite.collidepoint(mousePos):
					state = btn.onClick(state)
		return state
