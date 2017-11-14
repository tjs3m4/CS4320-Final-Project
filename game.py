# FORMAT FOR SPACING: a single tab for an indent
from enum import Enum
import pygame
import controller
import logicHandler
import graphicsManager

# create enumeration to represent state of the game
class GameState(Enum):
	MAIN_MENU = 0
	PAUSE_MENU = 1

# initialize screen
screenSize = (800, 800)
pygame.display.set_caption("") # sets the text on the top of the window

clock = pygame.time.Clock()

# list of ships and on-screen projectiles for game logic
bullets = []
ships = []

# initialize player controller
control = controller.Controller()
# add player ship to ship list
ships.append(control.player)

# initialize handler for game logic
logic = logicHandler.LogicHandler(bullets, ships)

# initialize manager for graphics
graphics = graphicsManager.GraphicsManager(bullets, ships)

# start game in main menu
state = GameState.MAIN_MENU

exit = False
while (not exit):
	# time based loop, 120 frames per second
	# clock.tick(120) # less accurate across platforms but less cpu intensive
	clock.tick_busy_loop(120) # more accurate across platforms but more cpu intensive

	# check for user inputs and exit game if requested by user
	exit = control.handleInputs(state)

	# update game logic
	logic.updateGameLogic()

	# update graphics on the screen to reflect the state of the game
	graphics.updateGraphics()