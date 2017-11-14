# the class responsible for managing the screen and drawing to it
import pygame

class GraphicsManager:
	def __init__(self, bullets, ships):
		screenSize = (800, 800)
		self.screen = pygame.display.set_mode(screenSize, pygame.DOUBLEBUF)
		self.bullets = bullets
		self.ships = ships

	def updateGraphics(self):			
		self.screen.fill((0,0,0))
		for ship in self.ships:
			self.screen.blit(ship.texture, ship.sprite)

		pygame.display.flip() # draw to the screen
		return
