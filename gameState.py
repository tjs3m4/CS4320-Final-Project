from enum import Enum
# represents the state that the game is currently in
class GameState(Enum):
	PLAYING = 0
	MAIN_MENU = 1
	PAUSE_MENU = 2
	GAME_EXIT = 3
	GAME_OVER = 4
	GAME_RESET = 5