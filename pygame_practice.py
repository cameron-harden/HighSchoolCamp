"""
title: pygame_practice
author: Cameron
date: 2019-06-14 09:52
"""
#import pygame

# Import a library of functions called 'pygame'
import pygame

# Initialize the game engine
pygame.init()

# Set the height and width of the screen
size = (400, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("First Pygame")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (205,133,63)

PI = 3.141592653



# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Speed in pixels per frame
x_speed = 0
y_speed = 0

# Current position
x_coord = 10
y_coord = 10

ball_pos = 0
ball_change = 1

def draw_stick_figure(screen, x, y):
    pygame.draw.ellipse(screen, RED, [130 + x, 525 + ball_pos + y, 40, 40])
    # pygame.draw.ellipse(screen, RED, [20, 200 + ball_pos, 40, 40])
    pygame.draw.circle(screen, BLACK, [200 + x, 190 + y], 120)
    pygame.draw.circle(screen, BROWN, [200 + x, 230 + y], 120)
    pygame.draw.polygon(screen, BLACK, [[198 + x, 220 + y], [202 + x, 230 + y], [198 + x, 240 + y]])
    pygame.draw.ellipse(screen, BLACK, [130 + x, 130 + y, 30, 95], 2)
    pygame.draw.ellipse(screen, BLACK, [235 + x, 130 + y, 30, 95], 2)
    # pygame.draw.arc(screen, BLACK, [50, 200, 100, 200], 0, PI / 2)

    pygame.draw.line(screen, BLACK, [200 + x, 350 + y], [200 + x, 600 + y], 5)
    pygame.draw.line(screen, BLACK, [200 + x, 600 + y], [160 + x, 800 + y], 5)
    pygame.draw.line(screen, BLACK, [200 + x, 600 + y], [240 + x, 800 + y], 5)
    pygame.draw.line(screen, BLACK, [200 + x, 400 + y], [160 + x, 535 + y], 5)
    pygame.draw.line(screen, BLACK, [200 + x, 400 + y], [240 + x, 535 + y], 5)

    pygame.draw.arc(screen, BLACK, [100 + x, 245 + y, 190, 60], PI, 0 / 2)
    # pygame.draw.ellipse(screen, BLUE, [160, 370, 80, 250], 2)
    # pygame.draw.polygon(screen, BROWN, [[180, 330], [220, 330], [220, 390], [180, 390]])
    # pygame.draw.polygon(screen, BLACK, [[180, 330], [220, 330], [210, 350], [190, 350]])
    #pygame.draw.polygon(screen, BLACK, [[180, 600], [220, 600], [210, 400], [190, 400]])

    #pygame.draw.ellipse(screen, BLUE, [160, 370, 80, 250], 2)
# Loop as long as done == False
while not done:
    ball_pos += ball_change

    if ball_pos > 215:
        ball_change -= 3
    elif ball_pos < 30:
        ball_change += 3
    # User did something
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x_speed = -3
    if keys[pygame.K_RIGHT]:
        x_speed = 3
    if keys[pygame.K_UP]:
        y_speed = -3
    if keys[pygame.K_DOWN]:
        y_speed = 3

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Move the object according to the speed vector.
    x_coord += x_speed
    y_coord += y_speed

    # Reset x_speed and y_speed for the next frame
    x_speed = 0
    y_speed = 0

    # Go ahead and update the screen with what we've drawn.
    screen.fill(WHITE)
    draw_stick_figure(screen, x_coord, y_coord)

    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)



# Be IDLE friendly
pygame.quit()
