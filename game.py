# FORMAT FOR SPACING: a single tab for an indent
from enum import Enum
import pygame
import controller
import logicHandler
import graphicsManager
import gameState
import button

# FUNCTIONS FOR CREATING THE MENUS
# --------------------------------
	# FUNCTIONS TO RUN WHEN A BUTTON IS CLICKED
def continueClk(state):
	return gameState.GameState.PLAYING

def exitGame(state):
	if state == gameState.GameState.PAUSE_MENU:
		return gameState.GameState.MAIN_MENU

	return gameState.GameState.GAME_EXIT

def playGame(state):
	return gameState.GameState.PLAYING

def createMainMenu(x, y):
	y -= 50
	buttons = {}

	# NOTE: in python, you cannot make an assignment inside a lambda. This make it difficult to change the gamestate with a lambda expresssion
	# in order to get around this, I am doing something similiar to function pointers in C++

	onClick = playGame # sets False for trigger to exit game
	buttons["play"] = button.Button("buttons/play_h.png", "buttons/play.png", onClick, x, y)	

	y += 50
	onClick = exitGame
	buttons["quit"] = button.Button("buttons/quit_h.png", "buttons/quit.png", onClick, x, y)

	return buttons

def createPauseMenu(x, y):
	y -= 50
	buttons = {}

	onClick = continueClk
	buttons["continue"] = button.Button("buttons/continue_h.png", "buttons/continue.png", onClick, x, y)

	y += 50
	onClick = exitGame
	buttons["quit"] = button.Button("buttons/quit_h.png", "buttons/quit.png", onClick, x, y)

	return buttons
# --------------------------------

# INITIALIZERS FOR GAME AND GAME OBJECTS
# --------------------------------------
# initialize state of the game
state = gameState.GameState.MAIN_MENU

#initialize screen size
screenSize = (1024, 800)

# initalize menus and have options shown at center screen
mMenu = createMainMenu(screenSize[0] / 2, screenSize[1] / 2)
pMenu = createPauseMenu(screenSize[0] / 2, screenSize[1] / 2)

# list of ships and on-screen projectiles for game logic
bullets = []
ships = []

# initialize handler for game logic
logic = logicHandler.LogicHandler(screenSize, bullets, ships)

# initialize manager for graphics
graphics = graphicsManager.GraphicsManager(screenSize, bullets, ships, mMenu, pMenu)

# initialize player controller
control = controller.Controller(graphics.screenSize, mMenu, pMenu)
# add player ship to ship list
ships.append(control.player)

# initialize clock for timed game loop
clock = pygame.time.Clock()
# --------------------------------------

# MAIN GAME LOOP
#---------------
exit = False
while (not state == gameState.GameState.GAME_EXIT):
	# time based loop, 120 frames per second
	# clock.tick(120) # less accurate across platforms but less cpu intensive
	clock.tick_busy_loop(120) # more accurate across platforms but more cpu intensive

	# check for user inputs and exit game if requested by user
	state = control.handleInputs(state)

	# update game logic
	logic.updateGameLogic(state)

	# update graphics on the screen to reflect the state of the game
	graphics.updateGraphics(state)
#---------------