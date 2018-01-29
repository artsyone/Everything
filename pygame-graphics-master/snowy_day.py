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
TITLE = "Sunny Day"
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

''' Make stars '''
stars = []
'span start here'
for i in range(600):
    x = random.randrange(-300, 1000)
    y = random.randrange(-500, 400)
    r = random.randrange(1, 5)
    s = [x, y, r, r]
    stars.append(s)




for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 200)
    loc = [x, y]
    clouds.append(loc)

def draw_cloud(loc):
    x = loc[0]
    y = loc[1]
    
    pygame.draw.ellipse(screen, GREY, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GREY, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GREY, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, GREY, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, GREY, [x + 20, y + 20, 60, 40])



def draw_cloud(loc):
    x = loc[0]
    y = loc[1]
    
    pygame.draw.ellipse(screen, GREY, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GREY, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GREY, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, GREY, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, GREY, [x + 20, y + 20, 60, 40])
   
# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Game logic
    
    for s in stars:
        s[1] += 2
        
        

        if s[1] > 800:
           s[0] = random.randrange(-500, 800)
           s[1] = random.randrange(-50, 0)


    
    for c in clouds:
        c[0] += 2

        if c[0] > 800:
           c[0] = random.randrange(-1600, -100)
           c[1] = random.randrange(-50, 200)
             
    # Drawing code
    ''' sky '''
    screen.fill(RGREY)

    ''' sun '''
       
   


    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])

    

    
    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)




    ''' stars '''
    for s in stars:
        pygame.draw.ellipse(screen, WHITE, s)
    

   
    ''' clouds '''
    for c in clouds:
        draw_cloud(c)

    

   


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
