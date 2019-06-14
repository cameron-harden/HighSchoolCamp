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

screen.fill(WHITE)

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Loop as long as done == False
while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Go ahead and update the screen with what we've drawn.
    pygame.draw.circle(screen, BLACK, [200, 190], 120)
    pygame.draw.circle(screen, BROWN, [200, 230], 120)
    pygame.draw.polygon(screen, BLACK, [[198, 220], [202, 230], [198, 240]])
    pygame.draw.ellipse(screen, BLACK, [130, 130, 30, 95], 2)
    pygame.draw.ellipse(screen, BLACK, [235, 130, 30, 95], 2)
    #pygame.draw.arc(screen, BLACK, [50, 200, 100, 200], 0, PI / 2)


    pygame.draw.line(screen, BLACK, [200, 350], [200, 600], 5)
    pygame.draw.line(screen, BLACK, [200, 600], [160, 800], 5)
    pygame.draw.line(screen, BLACK, [200, 600], [240, 800], 5)
    pygame.draw.line(screen, BLACK, [200, 400], [160, 535], 5)
    pygame.draw.line(screen, BLACK, [200, 400], [240, 535], 5)

    pygame.draw.arc(screen, BLACK, [100, 245, 190, 60], PI, 0 / 2)
    #pygame.draw.ellipse(screen, BLUE, [160, 370, 80, 250], 2)
   # pygame.draw.polygon(screen, BROWN, [[180, 330], [220, 330], [220, 390], [180, 390]])
    #pygame.draw.polygon(screen, BLACK, [[180, 330], [220, 330], [210, 350], [190, 350]])
    #pygame.draw.polygon(screen, BLACK, [[180, 600], [220, 600], [210, 400], [190, 400]])

    #pygame.draw.ellipse(screen, BLUE, [160, 370, 80, 250], 2)

    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)



# Be IDLE friendly
pygame.quit()
