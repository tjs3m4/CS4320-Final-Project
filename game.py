# FORMAT FOR SPACING: a single tab for an indent
from enum import Enum
import pygame
import controller

# create enumeration to represent state of the game
class GameState(Enum):
	MAIN_MENU = 0
	PAUSE_MENU = 1

# initialize screen and framerate
screen = pygame.display.set_mode((800,800), pygame.DOUBLEBUF)
pygame.display.set_caption("") # sets the text on the top of the window

clock = pygame.time.Clock()
deltat = clock.tick(30)

# initialize player controller
control = controller.Controller()

# list of enemy ships and on-screen projectiles
bullets = []
enemies = []

# start game in main menu
state = GameState.MAIN_MENU

exit = False
while (not exit):
	# check for user inputs and exit game if requested by user
	exit = control.handleEvent()

	# update game logic


	# update graphics on the screen to reflect the state of the game
	

	pygame.display.flip() # draw to the screen