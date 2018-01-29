# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "BORED"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
GREEN = (0, 175, 0)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)
GREY = (166, 166, 166)
BLACK = (0,0,0)
RGREY = (51, 51, 51)

# Make clouds
num_clouds = 30
clouds = []





for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 200)
    loc = [x, y]
    clouds.append(loc)



def draw_cloud(loc):
    x = loc[0]
    y = loc[1]
    
    pygame.draw.line(screen, GREEN, [x, y + 20, 40 , 40])
    pygame.draw.line(screen, YELLOW, [x + 60, y + 20, 40 , 40])
    pygame.draw.line(screen, BLUE, [x + 20, y + 10, 25, 25])
    pygame.draw.line(screen, BLACK, [x + 35, y, 50, 50])
    
    #pygame.draw.line(screen, RED, [x + 20, y + 20, 60, 40])
   
# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Game logic
    
   


    
    for c in clouds:
        c[0] += 2

        if c[0] > 800:
           c[0] = random.randrange(-1600, -100)
           c[1] = random.randrange(-50, 200)
             
    # Drawing code
    ''' sky '''
    screen.fill(WHITE)

    ''' sun '''
       
   


    ''' grass '''
       

    
    ''' fence '''
    




    ''' stars '''
    
    

   
    ''' clouds '''
    for c in clouds:
        draw_cloud(c)

    

   


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
