 import pygame
 import math



    def magnitude(v):
        return math.sqrt(sum(v[i]*v[i] for i in range(len(v))))
    def add(u,v):
        return [(a-b) for (a,b) in zip(u,v)]
    def dot(u,v):
        return sum((a*b) for (a,b) in zip(u,v))
    def sub(u,v):
        return sum((a*b) for (a,b) in zip(u,v))
    def normalize(v):
        vmag = magnitude(v)
        return [ v[i]/vmag for i in range(len(v)) ]

    def length(v):
        return math.sqrt(dot(v, v))
    def angle(v1, v2)
        return math.acos(dot(v1, v2) / (length(v1) * length(v2)))
    def get_image():


    def rot_center(image, angle):
        orig_rec = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image

class Bullet(object):
           surf = None
           def _init_(self):
              self.x, self.y = (0, 0)
              self.speed, self.angle = 10, 0
              self.target_vector = [0, 0]

          @property
           def img(self):
              if not self.surf:
                  self.surf = get_image()
              return self.surf
          @property
           def pos(self):
               return self.x, self.y

          @property
           def int_pos(self):
               return map(int, self.pos)
          @property
           def center_pos(self):
               return [a-16 for a in self.ini_pos]
            
           def update(self):
               if self.speed == 0:
                  return 
               move_vector = [ c * self.speed for c in normalize(self.target_vector)]

               self.x, self.y = add(self.pos, move_vector)





    def fire(start, angle, target_vector):
        act = Bullet()
        act.x, act.y = start
        act. angle = angle
        act.target_vector = target_vector
        return act

    
    def reset(self, position):
        self.rect.left, 
        self.active = True
        
