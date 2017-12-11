# Files
## [game.py](/game.py)
* Main game file, initializes the window, creates the graphicsManager, logicHandler, controller, menus, containers for game objects, and contains the main game logic loop.

## [graphicsManager.py](graphicsManager.py)
* Contains the GraphicsManager class that is responsible for displaying everything to the screen.

## [logicHandler.py](logicHandler.py)
* Contians the LogicHandler class which updates the state of the game.

## [controller.py](controller.py)
* Contains the Controller class that handles user input, controls the player ship, and handles navigation for the menus.

## ship.py
* Contains various that define what a Ship is. Has more specific subclasses like AdvancedShip, EnemyShip, and bullet.

## weapon.py
* Contains the Weapon class that defines what a weapon is.

## button.py
* Data structure that represents a clickable button that appears in the menus.

## gameState.py
* A simple enumeration for representing the current state the game is in. (PLAYING, PAUSED, MAIN_MENU, etc....)

# Classes and their Functionality
## Controller
* Handles user input events that move the ship around the screen, and events that navigate the menus.
* Has lists of Buttons which represent the menus
* Has an AdvancedShip that represents the player's ship
* Can alter the state of the game based on user input. (paused state, restarting, quitting)

## GraphicsManager
* Has access to the list of ships, bullets, and the menus.
* Responsible for refreshing the screen and drawing everything to it according to their position.

## LogicHandler
* Has access to the list of ships, bullets, and the menus.
* Updates the position of all ships and bullets.
* Handles collision detection and determines when to "destroy" ships.
* Handles spawing enemy ships, firing the player's weapon, and spawing upgrades for the player to collect.
* Manages the state of the game according to the player's health or existing state of the game.

## Button
* Has a function that is run when clicked on.
* Has an on and off state with an image associated with each one.

## Ship
* Base class that represents what a Ship is.
* Contains data necessary for representing a Ship.
* All ships derive from this base class.

## AdvancedShip
* Extends the functionality of a Ship to make it capable of firing a weapon.
* The player ship is of this type.

## EnemyShip
* Overwrites functionality of a ship to make it target the player's ship.

## Bullet
* Uses data from a ship, but overwrites some functionality because its logic for rotating and moving is different.

## Weapon
* Contains the data necessary to represent a weapon.
