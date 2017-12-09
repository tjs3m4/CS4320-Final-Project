# Files
	* game.py
		Main game file, initializes the window, data structure the game needs to run, and contains the main game logic loop.

	* controller.py
		Contains the Controller class that handles user input, controls the player ship, and handles navigation for the menus.

	* ship.py
		Contains the classes that define what a Ship and AdvancedShip are, as well as their functions.

	* weapon.py
		Contains the Weapon class that defines what a weapon is.

	* bullet.py
		Contains the Bullet class that defines what a bullet is.
        * Logichandler.py
	        * Class used to keep track of and update the game logic as the game plays.
		* Contains updating the weapons, bullets, ships
		
	* Graphichandler.py
	        * Contain displaying the mainMenu, changes of the screen, the background images as the player's flight moves around
		* Update the game state whenever the player chooses starting the game or pause it
		* Contain scrolling down the wallpaper
	
## Classes and their Functionality
	* Controller
		* Handles user input events that move the ship around the screen, and events that navigate the menus.
		* Has an AdvancedShip that represents the player's ship

	* Ship
		* Base class that represents what a Ship is.
		* Contains data necessary for representing a Ship.
		* Basic enemy ships are of this type.

	* AdvancedShip
		* Is a Ship
		* Extends the functionality of a Ship to make it capable of firing a weapon
		* The player ship and boss ships are of this type

	* Weapon
		* Contains the data necessary to represent a weapon.
		* Has a Bullet

	* Bullet
		* Contains the data necessary to represent a bullet.
	* GraphicsManager
	        * Manage the scrolling of wallpaper, the main menu, which contains "play" and "quit"
	* GameState
	        * Contains the enum value corresponding to the state of the game
	* EnemyShip:
	        * Contains the image, the health as the attributes of enemyship, and "accelerate, move, rotate" as the behavior of the                   * enemy ship
	* AdvancedEnemyShip:
	        * The boss ship
	
	
	
## Summary of how classes interact
	* The Controller controls a player's ship (which is of type AdvancedShip).
	* An Advanced ship has a Weapon which has Bullets to shoot.
	
