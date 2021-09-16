# Level-1-Capstone-Project-2
## A simple game
### This is a game where the user needs to collide with a prize object to win, without colliding with "enemy" objects. If the user collides with enemy objects, the user looses.
### The following objects are created:
1. Player object
2. Prize object
3. Three enemy objects
### *Player object*
#### The user object has the following properties:
* Can move in all 4 directions using the arrow keys
* Size of player image is imported from the pygame library using the get_height and get_width functions 
* Set starting point at x-axis 650 and y-axis 300 relative to the set screen size
### *Prize object*
#### The prize object has the following properties:
* Size of prize image is imported from the pygame library using the get_height and get_width functions 
* Set starting point at x-axis 1300 and random starting point along the y-axis using the random function, relative to the set screen size
### *Enemy objects*
#### The enemy objects have the following properties:
* Sizes of enemy images are imported from the pygame library using the get_height and get_width functions 
* Enemy object 1 (enemy) has a set starting point at y-axis equal to the screen width and random starting point along the x-axis using the random function.
* Enemy object 2 (monster) has a set starting point at y-axis equal to the screen width and random starting point along the x-axis using the random function.
* Enemy object 3 (bandit) has a set starting point at x-axis equal to the screen width and random starting point along the y-axis using the random function.
* Bounding boxes are used to creat boundaries around the objects, that will check if the player object collides with the enemy objects. 
### Outcomes:
1. Sizes regarding each object is displyed on screen to the user
2. If the user collides with the prize object, a message "You win!" will be displayed and the program quits
3. If the user collides with an enemy object, a message "You loose" will be displayed and the program quits
4. If the user enters '0' the game will quit
