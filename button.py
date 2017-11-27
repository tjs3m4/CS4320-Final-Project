import pygame

class Button:
	def __init__(self, onImage, offImage, onClick, x, y):
		self.onTexture = pygame.image.load(onImage) # the image itself
		self.offTexture = pygame.image.load(offImage) # the image itself
		self.activeTexture = self.offTexture # which image is to be displayed

		self.sprite = self.onTexture.get_rect(center = (x, y)) # the rectangle which the image is drawn onto

		self.onClick = onClick # function to run when button is clicked on

	def hover(self):
		self.activeTexture = self.onTexture

	def setInactive(self):
		self.activeTexture = self.offTexture