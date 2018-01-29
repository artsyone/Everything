Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Imports
import pygame
import math

# Initialize game engine
pygame.init()


# Window
SIZE = (900, 800)
TITLE = "My Awesome Picture"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
RED = (250, 24, 31)
REDL = (255, 159, 163)
GREEN = (0, 255, 0)
BLUE = (33, 65, 103)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125 , 0)
GREY = (196, 196, 196)
DAGREY = (58, 59, 61)
    

# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, [235, 245, 300, 215])
    pygame.draw.line(screen, GREEN, [380, 190], [250,50], 5)
    pygame.draw.line(screen, GREEN, [380, 190], [250,50], 5)
    pygame.draw.line(screen, BLACK, [380, 190], [,50], 5)
    
    pygame.draw.rect(screen, RED, [340, 190, 100, 50])
    pygame.draw.rect(screen, REDL, [340, 198, 100, 50],1)
    pygame.draw.rect(screen, RED, [220, 200, 340, 240])
  
    pygame.draw.rect(screen, WHITE, [240, 220, 300, 200])
    pygame.draw.rect(screen, BLACK, [245, 225, 290, 190])
    pygame.draw.rect(screen, BLUE, [255, 235, 200, 170])
    pygame.draw.rect(screen, GREY, [255, 235, 200, 170])
    pygame.draw.rect(screen, BLACK, [270, 240, 170, 160])
    pygame.draw.rect(screen, BLUE, [275, 245, 160, 150])
    
    

    pygame.draw.rect(screen, GREY, [470, 235, 50, 170])
    
    pygame.draw.rect(screen, BLACK, [475, 340, 40, 60],1)
    pygame.draw.rect(screen, BLACK, [475, 340, 40, 0],1)
    
    pygame.draw.rect(screen, BLACK, [475, 340, 40, 50],1)
 
    pygame.draw.rect(screen, BLACK, [475, 340, 40, 51],1)
    
    pygame.draw.rect(screen, BLACK, [475, 340, 40, 40],1)
    pygame.draw.rect(screen, BLACK, [475, 340, 40, 41],1)
    
    pygame.draw.rect(screen, BLACK, [475, 340, 40, 30],1)
    pygame.draw.rect(screen, BLACK, [475, 340, 40, 31],1)
    
    pygame.draw.rect(screen, BLACK, [475, 340, 40, 20],1)
    
    pygame.draw.rect(screen, BLACK, [475, 340, 40, 21],1)
    
    pygame.draw.rect(screen, BLACK, [475, 340, 40, 10],1)
    pygame.draw.rect(screen, BLACK, [475, 340, 40, 11],1)
    
    
    
    
   
    
    
    #pygame.draw.line(screen, GREEN, [300, 40], [100,500], 5)
   # pygame.draw.ellipse(screen, BLUE, [100, 100, 600, 300])
    #pygame.draw.polygon(screen, BLACK, [[200, 200], [50,400], [600, 500]], 10)

    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    #pygame.draw.arc(screen, ORANGE, [100, 100, 100, 100], 0, math.pi/2, 1)
    #pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi/2, 50)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
