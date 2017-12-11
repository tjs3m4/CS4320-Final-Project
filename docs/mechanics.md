# Game Mechanics

## Player
* The goal of the game is to survive as long as possible by avoiding enemy ships. The enemy ships will attempt to crash into you, but the player can destroy them with his/her weapon. The player has 3 health, and every time an enemy collides with the player, 1 health will be taken away. The remaining health value is displayed in the bottom-left corner of the screen.
* The weapon fires automatically, but you can adjust the projectile speed by positioning the mouse cursor further (faster projectile) or closer (slower projectile) to the ship. The distance of the mouse cursor to the ship also determines how fast or slowly the ship accelerates.
* The player cannot leave the screen. If the player hits the edge of the screen, the player's ship will bounce off and change direction, while also losing some of its velocity. This will not cause the player to take damage.

## Smaller ships
* Smaller ships fly in from any side of the screen. Which side is determined at random. The ships will persue the player until they are destroyed.
* Smaller ships can leave the screen and enter again without penalty.

## Upgrade
* Occassionally, a weapon supply will drop from the top of the screen. If the player can get this (my flying over it), the ship's rate of fire will increase by 20% for the remainder of the game. This effect stacks, meaning that for every supply you get, the fire rate will get even faster.
