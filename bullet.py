class Bullet:
        surf = None
	def __init__(self, x, y, velX, velY, image,speed, target_vector):
		self.velX = 0 # speed of ship in the X direction, used to update position on screen every iteration of game loop
		self.velY = 0 # speed of the ship in the Y direction
		self.angle = 0 # an angle, represents the direction the ship is facing
		self.damage = 0 # value representing the amount of damage the bullet will do
		self.texture = 0 # image represtenting the bullet
		self.sprite = 0 # the rectangle the bullet is drawn to
                self.speed = 2 #the speed of bullet
                self.target_vector = [0,0] #the x, y coordinates of the target we are going to hit

        def img(self):
            if not self.surf:
                self.surf = get_image()#A function allowing to get the image of the bullet(1)
               return self.surf

        def pos(self):
            return self.velX, self.velY #return the position of the bullet

        def int_pos(self):
            return map(int, self.pos) #apply int function to self.pos make the x and y coordinates as the integer

        def center_pos(self):
            return [a-16 for a in self.int_pos]#doing some calculation to ensure the center position

        def update(self):
            if self.speed == 0:
                return

            #apply speed to target_vector
            move_vector = [c * self.speed for c in normalize(self.target_vector)]
            

            #update position by adding the position vector to movement vector
            self.x, self.y = add(self.pos, move_vector)

#triangle theory from the math
def magnitude(v):
    return math.sqrt(sum(v[i]*v[i] for i in range(len(v))))

#adding the target_vector to the move vector
def add(u, v):
    return [(a+b) for (a, b) in zip(u, v)]

def sub(u, v):
    return [(a-b) for (a, b) in zip(u, v)]
def dot(u, v):
    return sum((a*b) for a, b in zip(u, v))
def normalize(v):
    vmag = magnitude(v)
    return [ v[i]/vmag for i in range(len(v)) ]
def length(v):
    return math.sqrt(dot(v, v))

def angle(v1, v2):
    return math.acos(dot(v1, v2) / (length(v1) * length(v2)))

def get_image():
    surf = pygame.image.load()
    return image 









            
        
            

        
        
