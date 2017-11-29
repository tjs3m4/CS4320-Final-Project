# Game Mechanics

## Player
* Player moves according to its velocity. The velocity is changed by accelerating in a direction.
  * To slow the ship down, you must accelerate in the opposite direction, or collide with the side of the screen.
* The player cannot move outside the bounds of the window.
  * A collision with any side will cause the player to bouce off and lose velocity.

## Smaller ships
* Smaller ships can come from any side of the screen.

## Larger (Boss) Ships
* Spawn in from the top of the screen.
* They have a weapon and are capable of firing at the player. 
  * They will drop their weapon on destruction and they player can pick it up for their arsenal.
* They will move to avoid crashing into the player.
