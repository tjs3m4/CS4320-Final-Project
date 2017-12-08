import math
from pygame.math import Vector2
import pygame as pg

pg.init()
BULLET_IMAGE = pg.Surface((20, 11), pg.SRCALPHA)
pg.draw.polygon(BULLET_IMAGE, pg.Color('grey11'), [(0, 0), (20, 5), (0, 11)])




class Bullet:
	def __init__(self, pos, angle):
	    self.image = pg.transform.rotate(BULLET_IMAGE, -angle)
	    self.rect = self.image.get_rect(center=pos)
	    #Apply offset to start position,
	    #create another vector and rotate this vector as well
	    vector = Vector2(50,0).rotate(angle)
	    #add the rotated vector to the position vector
	    self.pos = Vector2(pos) + offset
	    #Rotate the velocity vector (9,0) by the angle.
	    self.velocity = Vector(9, 0).rotate(angle)
