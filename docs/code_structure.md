# Files
* game.py
  * Main game file, initializes the window, data structures the game needs to run, and contains the main game logic loop.
  * Also defines the functions for, and initializes, the main menu and pause menu.
  
* logicHandler.py
  * The class responsible for updating the game logic every iteration of the game loop.
    * This includes things like position of all ships and bullets, as well as collision detection.
  
* graphicsManager.py
  * The class responsible for creating and updating the visual display of the game.

* controller.py
  * Contains the Controller class that handles user input, controls the player's ship, and handles navigation for the menus.

* ship.py
  * Contains the classes that define ship structures as well as their functions.

* weapon.py
  * Contains the Weapon class that defines what a weapon is.

* bullet.py
  * Contains the Bullet class that defines what a bullet is.
  
* button.py
  * Defines a button class that is used to create and interact with menu options.
  
* gameState.py
  * A simple class that defines an enumeration to represent the current state of the game.
  
## Simple Architecture
The code is organized according to a model-view-controller architecture.
* The Model
  * The ships and bullets on the screen are held in two lists.
  * The LogicHandler class updates the position of the ships and bullets on every iteration of the game loop.
    * It also looks for collisions.
    
* The View
  * The GraphicsManager class is responsible for managing the window and drawing all ships and bullets to the screen every game loop.
    * It also handles displaying the menu options and greying out actors when a menu needs to be displayed.
    
* The Controller
  * The Controller class checks for player input every iteration of the game loop, and handles the input event accordingly.
    * Handles both player ship movement and menu navigation.
