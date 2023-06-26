import pygame
import random

# Initialize pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the car
car_width = 73
car_height = 82
car_img = pygame.image.load("car.png")

def car(x, y):
    window.blit(car_img, (x, y))

# Set up the obstacles
def obstacles(obstacle_x, obstacle_y, obstacle_w, obstacle_h, color):
    pygame.draw.rect(window, color, [obstacle_x, obstacle_y, obstacle_w, obstacle_h])

# Set up game variables
clock = pygame.time.Clock()
car_x = (WIDTH - car_width) / 2
car_y = HEIGHT - car_height - 10
car_speed = 0

obstacle_width = 100
obstacle_height = 100
obstacle_x = random.randint(0, WIDTH - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 4

score = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car_speed = -5
            elif event.key == pygame.K_RIGHT:
                car_speed = 5

        # Check for key releases
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                car_speed = 0

    # Move the car
    car_x += car_speed

    # Keep the car within the window bounds
    if car_x < 0:
        car_x = 0
    elif car_x > WIDTH - car_width:
        car_x = WIDTH - car_width

    # Move the obstacles
    obstacle_y += obstacle_speed

    # Check for collision with the car
    if car_y < obstacle_y + obstacle_height:
        if car_x < obstacle_x < car_x + car_width or car_x < obstacle_x + obstacle_width < car_x + car_width:
            # Collision occurred
            running = False

    # Check if the obstacle passed the car
    if obstacle_y > HEIGHT:
        obstacle_y = -obstacle_height
        obstacle_x = random.randint(0, WIDTH - obstacle_width)
        score += 1

    # Fill the window with white color
    window.fill(WHITE)

    # Draw the car
    car(car_x, car_y)

    # Draw the obstacles
    obstacles(obstacle_x, obstacle_y, obstacle_width, obstacle_height, RED)

    # Display the score
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, BLACK)
    window.blit(text, (10, 10))

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
