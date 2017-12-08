import math
from pygame.math import Vector2
import pygame





class Bullet:
	def __init__(self, image, x, y, pos, angle):
	    self.x = x
	    self.y = y
	    self.masterTexture = image
	    self.texture = self. masterTexture
	    self.sprite = image.get_rect(center = (self.x, self.y))
	    #Apply offset to start position,
	    #create another vector and rotate this vector as well
	    vector = Vector2(50,0).rotate(angle)
	    #add the rotated vector to the position vector
	    self.pos = Vector2(pos) + vector
	    #Rotate the velocity vector (9,0) by the angle.
	    self.velocity = Vector(9, 0).rotate(angle)
       def  update(self)
            self.pos += self.velocity
            self.sprite.center = self.pos
