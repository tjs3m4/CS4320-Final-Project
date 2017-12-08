import math
from pygame.math import Vector2
import pygame





class Bullet:
	def __init__(self, image, x, y, pos, angle):
	    x, y = Vector2(pg.mouse.get_pos()) - cannon.center
            angle = math.degrees(math.atan2(y, x))
	    self.image =  pygame.transform.rotate(image, -angle)
	    self.sprite = self.image.get_rect(center = pos)
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
