
import pygame  # Imports a game library that lets you use specific functions in your program.
import random  # Import to generate random numbers.

# Initialize the pygame modules to get everything started.

pygame.init()

# The screen that will be created needs a width and a height.
# The screen size is increase as more images are on it.
screen_width = 1300
screen_height = 750

# This creates the screen and gives it the width and height specified as a 2 item sequence.
screen = pygame.display.set_mode((screen_width, screen_height))

# This creates the player and gives it the image found in this folder (similarly with the 'enemy', 'monster', 'bandit'
# and 'prize').
player = pygame.image.load("image.png")
enemy = pygame.image.load("enemy.png")
monster = pygame.image.load("monster.jpg")  # Added another enemy called 'monster'
bandit = pygame.image.load("bandit.jpg")  # Added another enemy called 'bandit'
prize = pygame.image.load("prize.jpg")  # Added a prize called 'prize'

# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within
# screen boundaries or know when the image is off the screen).

image_height = player.get_height()
image_width = player.get_width()

enemy_height = enemy.get_height()
enemy_width = enemy.get_width()

# Added width and height for monster to detect the boundaries.
# (Similar for 'bandit' and 'prize' below)
monster_height = monster.get_height()
monster_width = monster.get_width()

bandit_height = bandit.get_height()
bandit_width = bandit.get_width()

prize_height = prize.get_height()
prize_width = prize.get_width()

# Dimensions information about the images in the game
print("\nThis is the height of the player image: " + str(image_height))
print("This is the width of the player image: " + str(image_width))

print("\nThis is the height of the enemy image: " + str(enemy_height))
print("This is the width of the enemy image: " + str(enemy_width))

print("\nThis is the height of the monster image: " + str(monster_height))
print("This is the width of the monster image: " + str(monster_width))

print("\nThis is the height of the bandit image: " + str(bandit_height))
print("This is the width of the bandit image: " + str(bandit_width))

print("\nThis is the height of the prize image: " + str(prize_height))
print("This is the width of the prize image: " + str(prize_width))

# Store the positions of the images as variables so that it can be changed later.
# Position of 'player' is changed to the centre of screen to prevent any initial collision before the game starts
playerXPosition = 650
playerYPosition = 300

# Make the enemy start off screen and at a random y position.
enemyXPosition = screen_width
enemyYPosition = random.randint(0, screen_height - enemy_height)

# 'monster' starts off screen with X position being random
monsterYPosition = screen_width
monsterXPosition = random.randint(0, screen_height - monster_height)

# 'bandit' starts at X-coordinate = 0 with Y position being random
banditXPosition = 0
banditYPosition = random.randint(0, screen_height - bandit_height)

# 'prize' position is stored to be on the opposite end of 'player' with X-coordinate = 1300
prizeXPosition = 1300
prizeYPosition = random.randint(0, screen_height - prize_height)

# This checks if the up or down key is pressed.
# Right now they are not so make them equal to the boolean value (True or False) of False.
# Boolean values are True or False values that can be used to test conditions and test states that are binary,
# i.e. either one way or the other.

keyUp = False
keyDown = False

# This checks if the left or right keys are pressed.
# These keys are made equal to the boolean value False.
keyLeft = False
keyRight = False

# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to represent real time game play.

while 1:  # This is a looping structure that will loop the indented code until you tell it to stop(in the event where
    # you exit the program by quitting). In Python the int 1 has the boolean value of 'true'. In fact numbers greater
    # than 0 also do. 0 on the other hand has a boolean value of false. You can test this out with the
    # bool(...) function to see what boolean value types have. You will learn more about while loop structures later.

    screen.fill(0)  # Clears the screen.

    # This draws the player image to the screen at the position specified i.e. (650, 300).
    screen.blit(player, (playerXPosition, playerYPosition))

    screen.blit(enemy, (enemyXPosition, enemyYPosition))

    # These three images were added to the game to increase difficulty.
    # This draws the images to the screen with the specified positions as specified above.
    screen.blit(monster, (monsterXPosition, monsterYPosition))
    screen.blit(bandit, (banditXPosition, banditYPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))

    pygame.display.flip()  # This updates the screen.

    # This loops through events in the game.
    for event in pygame.event.get():

        # This event checks if the user quits the program, then if so it exits the program.
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # This event checks if the user presses a key down.
        if event.type == pygame.KEYDOWN:

            # Test if the key pressed is the one we want.
            if event.key == pygame.K_UP:  # pygame.K_UP represents a keyboard key constant.
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True

        # This event checks if the key is up(i.e. not pressed by the user).
        if event.type == pygame.KEYUP:

            # Test if the key released is the one we want.
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False

        # This event checks if the user presses a key down.
        if event.type == pygame.KEYDOWN:

            # Test if the key pressed is the one we want.
            if event.key == pygame.K_LEFT:      # pygame.K_LEFT represents a keyboard key constant.
                keyLeft = True
            if event.key == pygame.K_RIGHT:     # pygame.K_RIGHT represents a keyboard key constant.
                keyRight = True

        # This event checks if the key is up (i.e. not pressed by the user).
        if event.type == pygame.KEYUP:

            # Test if the key released is the one we want.
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False

    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.

    # The coordinate system of the game window (screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position.

    if keyUp:  # Simplified, same as 'if keyUp == True'

        if playerYPosition > 0:  # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1

    if keyDown:  # Simplified, same as 'if keyDown == True'

        if playerYPosition < screen_height - image_height:  # This makes sure that the user does not move the player
            # below the window.

            playerYPosition += 1

    if keyLeft:  # Simplified, same as 'if keyLeft == True'

        if playerXPosition > 0:  # This makes sure that the user does not move the player above the window.
            playerXPosition -= 1

    if keyRight:  # Simplified, same as 'if keyRight == True'

        if playerXPosition < screen_width - image_width:  # This makes sure that the user does not move the player
            # below the window.

            playerXPosition += 1

    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We then need to test if these boxes intersect. If they do then there is a collision.

    # Bounding box for the player:
    playerBox = pygame.Rect(player.get_rect())

    # The following updates the playerBox position to the player's position, in effect making the box stay around
    # the player image.
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    # Bounding box for 'enemy':
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    # Bounding boxes are also needed for 'monster', 'bandit' and 'prize' to check collision with 'player'
    # Collision with 'monster' and 'bandit' will result in losing the game
    # Collision with 'prize' will result in winning the game

    # Bounding box for 'monster':
    monsterBox = pygame.Rect(monster.get_rect())
    monsterBox.top = monsterYPosition
    monsterBox.left = monsterXPosition

    # Bounding box for 'bandit':
    banditBox = pygame.Rect(bandit.get_rect())
    banditBox.top = banditYPosition
    banditBox.left = banditXPosition

    # Bounding box for 'prize':
    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

    # Test collision of the boxes:
    if playerBox.colliderect(enemyBox):
        # Display losing status to the user:
        print("\nYou lose!")

        # Quite game and exit window:
        pygame.quit()
        exit(0)

    if playerBox.colliderect(monsterBox):
        # Display losing status to the user:
        print("\nYou lose!")

        # Quite game and exit window:
        pygame.quit()
        exit(0)

    if playerBox.colliderect(banditBox):
        # Display losing status to the user:
        print("\nYou lose!")

        # Quite game and exit window:
        pygame.quit()
        exit(0)

    # This is the only winning condition, to collide with 'prize'. If the other images moves off the screen before
    # you collide with 'prize', you lose.
    if playerBox.colliderect(prizeBox):
        # Display winning status to the user:
        print("\nYou win!")

        # Quite game and exit window:
        pygame.quit()
        exit(0)

    # If the enemy is off the screen the user loses the game. This forces the user to obtain the prize before this
    # happens
    if enemyXPosition < 0 - enemy_width:
        # Display losing status to the user:
        print("\nYou lose!")

        # Quite game and exit window:
        pygame.quit()

        exit(0)

    # If the enemy is off the screen the user loses the game. This forces the user to obtain the prize before this
    # happens
    if monsterYPosition < 0 - monster_height:
        # Display losing status to the user:
        print("\nYou lose!")

        # Quite game and exit window:
        pygame.quit()

        exit(0)

    # Different speeds were chosen to make the game more difficult
    # The time taken for 'enemy' to leave the screen was calculated to be the same as the time taken for 'monster' to
    # leave the screen, to increase difficulty of the game by forcing the user to play under pressure.
    # time = (distance/speed)

    # Make enemy approach the player.
    enemyXPosition -= 0.29

    monsterYPosition -= 0.3     # 'monster' moves along the Y-axis
    banditXPosition += 0.1      # 'bandit' moves in the opposite direction to 'enemy' on the X-axis
    prizeXPosition -= 0.05      # 'prize moves along the X-axis. Starts on the opposite side of 'player'

    # ================The game loop logic ends here. =============

# References:
# 'bandit' image (called Raccoon Bandit) - https://www.pngwing.com/en/search?q=bad+Guy
# https://www.w3schools.com/python/python_for_loops.asp
# https://www.w3schools.com/python/python_conditions.asp
# https://realpython.com/python-boolean/
# https://www.pygame.org/docs/ref/image.html
