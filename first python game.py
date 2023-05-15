import pygame
import random

# Initialize pygame
pygame.init()

# Set the window size
size = (1100, 700)
screen = pygame.display.set_mode(size)

# Set the window title
pygame.display.set_caption("Two-Player Game")

# Set the color of the players
red = (255, 0, 0)
green = (0, 255, 0)

# Set the color of the collectible
blue = (0, 0, 255)

# Set the size of the players and collectible
player_size = 50
item_size = 50

# Set the initial positions for the player squares
player1_x, player1_y = size[0]//2, size[1]//2
player2_x, player2_y = size[0]//2, size[1]//2

# Set the initial position for the collectible
item_x, item_y = size[0]//2, size[1]//2

# Set the initial scores
player1_score = 0
player2_score = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get player 1's movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player1_x -= 5
    if keys[pygame.K_RIGHT]:
        player1_x += 5
    if keys[pygame.K_UP]:
        player1_y -= 5
    if keys[pygame.K_DOWN]:
        player1_y += 5

    # Get player 2's movement
    if keys[pygame.K_a]:
        player2_x -= 5
    if keys[pygame.K_d]:
        player2_x += 5
    if keys[pygame.K_w]:
        player2_y -= 5
    if keys[pygame.K_s]:
        player2_y += 5
        
      
    # clear the screen
    screen.fill((255, 255, 255))
        
    # Check if player 1 collides with the collectible
    if (
        player1_x < item_x + item_size
        and player1_x + player_size > item_x
        and player1_y < item_y + item_size
        and player1_y + player_size > item_y
    ):
        player1_score += 1
        item_x, item_y = random.randint(0, size[0]), random.randint(0, size[1])
   
 # Check if player 2 collides with the collectible
    if (
        player2_x < item_x + item_size
        and player2_x + player_size > item_x
        and player2_y < item_y + item_size
        and player2_y + player_size > item_y
    ):
        player2_score += 1
        item_x, item_y = random.randint(0, size[0]), random.randint(0, size[1])



    # Check if either player goes out of the screen
    if player1_x < 0:
        player1_x = 650
    elif player1_x > 650:
        player1_x = 0
    if player1_y < 0:
        player1_y = 450
    elif player1_y > 450:
        player1_y = 0

    if player2_x < 0:
        player2_x = 650
    elif player2_x > 650:
        player2_x = 0
    if player2_y < 0:
        player2_y = 450
    elif player2_y > 450:
        player2_y = 0

  # Draw the player1 square at the new position
pygame.draw.rect(screen, red, (player1_x, player1_y, 50, 50))
pygame.draw.rect(screen, green, (player2_x, player2_y, 50, 50))

# Draw the collectible at the new position
pygame.draw.rect(screen, blue, (item_x, item_y, 50, 50))


# Draw the score for player 1
font = pygame.font.Font(None, 30)
text = font.render("Player 1 Score: " + str(player1_score), True, (255, 255, 255))
screen.blit(text, (10, 20))

# Draw the score for player 2
font = pygame.font.Font(None, 30)
text = font.render("Player 2 Score: " + str(player2_score), True, (255, 255, 255))
screen.blit(text, (450, 20))
    
       # Update the display
pygame.display.update()

    # Pause for a moment
pygame.time.delay(10)

    
    # Exit the game
pygame.quit()
