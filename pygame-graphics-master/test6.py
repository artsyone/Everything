# Imports
import pygame
import math
import random

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 500)
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
BLUE1 = (33,65,255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125 , 0)
GREY = (196, 196, 196)
DAGREY = (58, 59, 61)
LGREY = (162, 169, 179)
YELLOW =(255,125,0) # not really yellow
FGREEN =(34,139,34)

num_clouds = 20
clouds = []
for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 200)
    loc = [x, y]
    clouds.append(loc)

colors = [RED,REDL,ORANGE,YELLOW]
xgoes =[300,310,320,330,340,350,369,370,380,390,400]
ygoes =[315,320,325,330,335]



c = colors[random.randint(0,len(colors)-1)]
xa = xgoes[random.randint(0,len(xgoes)-1)]
ya = ygoes[random.randint(0,len(ygoes)-1)]

xb = xgoes[random.randint(0,len(xgoes)-1)]
yb = ygoes[random.randint(0,len(ygoes)-1)]

xc = xgoes[random.randint(0,len(xgoes)-1)]
yc = ygoes[random.randint(0,len(ygoes)-1)]

b = [(pygame.draw.line(screen, GREEN, [489, 328], [489,314], 3)),(pygame.draw.line(screen, GREEN, [475, 314], [489,314], 3)),(pygame.draw.line(screen,WHITE, [489, 300], [489,314], 3)),(pygame.draw.line(screen,GREEN, [502, 314], [489,314], 3))]
def draw_cloud(loc):
    x = loc[0]
    y = loc[1]
    
    pygame.draw.ellipse(screen, WHITE, [x +10, y + 20, 20 , 20])
    pygame.draw.ellipse(screen, WHITE, [x + 50, y + 20, 20 , 20])
    pygame.draw.ellipse(screen, WHITE, [x + 25, y + 10, 15, 15])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 30, 30])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 40, 20])


def draw_flower(xa,ya,c):
    
    
    pygame.draw.ellipse(screen, c, [xa +0, ya + 14, 10 , 10])
    pygame.draw.ellipse(screen, c, [xa +5, ya + 20, 10 , 10])
    pygame.draw.ellipse(screen, c, [xa +0, ya + 25, 10 , 10])

    pygame.draw.ellipse(screen, c, [xa - 5, ya +20, 10 , 10])
    pygame.draw.ellipse(screen, BLACK, [xa + 3, ya + 22, 7.5 , 7.5])


def draw_flower1(xb,yb,c):
    
    
    pygame.draw.ellipse(screen, c, [xb +0, yb + 14, 10 , 10])
    pygame.draw.ellipse(screen, c, [xb +5, yb + 20, 10 , 10])
    pygame.draw.ellipse(screen, c, [xb +0, yb + 25, 10 , 10])

    pygame.draw.ellipse(screen, c, [xb - 5, yb +20, 10 , 10])
    pygame.draw.ellipse(screen, BLACK, [xb + 3, yb + 22, 7.5 , 7.5])


def draw_flower2(xc,yc,c):
    
    
    pygame.draw.ellipse(screen, c, [xc +0, yc + 14, 10 , 10])
    pygame.draw.ellipse(screen, c, [xc +5, yc + 20, 10 , 10])
    pygame.draw.ellipse(screen, c, [xc +0, yc + 25, 10 , 10])

    pygame.draw.ellipse(screen, c, [xc - 5, yc +20, 10 , 10])
    pygame.draw.ellipse(screen, BLACK, [xc + 3, yc + 22, 7.5 , 7.5])  

def draw_bush(x, y):
    pygame.draw.ellipse(screen, FGREEN, [x +10, y + 20, 20 , 20])
    pygame.draw.ellipse(screen, FGREEN, [x + 50, y + 20, 20 , 20])
    pygame.draw.ellipse(screen, FGREEN, [x + 25, y + 10, 15, 15])
    pygame.draw.ellipse(screen, FGREEN, [x + 35, y, 30, 30])
    pygame.draw.rect(screen, FGREEN, [x + 20, y + 20, 40, 20])
    pygame.draw.ellipse(screen, FGREEN, [x + 25, y, 30, 30])
    pygame.draw.ellipse(screen, FGREEN, [x + 15, y, 30, 30])




# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # Game logic (Check for collisions, update points, etc.)
    for s in clouds:
        s[0] -= 2

        if s[0] < -100:
           s[0] = random.randrange(800, 1600)
           s[1] = random.randrange(-50, 200)


    
    ''' leave this section alone for now ''' 

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    # Drawing code
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, [235, 245, 300, 215])
    

    pygame.draw.line(screen, BLACK, [390, 190], [250,50], 5)
    pygame.draw.line(screen, BLACK, [400, 190], [520,50], 5)
    
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

   



   

    

    pygame.draw.rect(screen, LGREY, [274, 253, 162, 130])
   

  
    ''' sky '''
    
    pygame.draw.rect(screen, BLUE1, [274, 253, 162, 130])
    ''' sun '''
    pygame.draw.ellipse(screen, YELLOW, [400, 260, 28, 28])

    ''' clouds '''

    for s in clouds:
        draw_cloud(s)

    
    
    #draw_cloud(274, 260)
    #draw_cloud(344, 270)
    
    #draw_cloud(650, 100)

    
    

    
    ''' grass '''
    pygame.draw.rect(screen, GREEN, [275, 375, 163, 20])


    draw_bush(250,335)
    draw_bush(300,335)
    draw_bush(350,335)
    draw_bush(375,335)


    draw_flower(xa,ya,c)
    draw_flower1(xb,yb,c)
    draw_flower2(xc,yc,c)
    

    ''' fence '''
    y = 350
    for x in range(279, 431, 29):
        pygame.draw.polygon(screen,WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [275, 370], [437, 370], 5)
    pygame.draw.line(screen, WHITE, [275, 380], [437, 380], 5)
    #pygame.draw.line(screen, GREEN, [300, 40], [100,500], 5)
   # pygame.draw.ellipse(screen, BLUE, [100, 100, 600, 300])
    #pygame.draw.polygon(screen, BLACK, [[200, 200], [50,400], [600, 500]], 10)
   
   

     
    pygame.draw.ellipse(screen, BLACK, [475, 250, 28, 28])
    pygame.draw.ellipse(screen, BLACK, [475, 300, 28, 28])

    
    postions = [489, 250, 489,264],[475, 264, 489,264],[489, 277, 489,264],[502, 264,489,264]
  

    knobp = [489, 328,489,314],[475, 314, 489,314],[489, 300, 489,314],[502, 314,489,314]
    



       

    def knob():
             postion = postions[random.randint(0,3)]
             pygame.draw.line(screen, WHITE, postion[0:2],postion[2:4],3)

    def knob2():
             postion = knobp[random.randint(0,3)]
             pygame.draw.line(screen, WHITE, postion[0:2],postion[2:4],3)

           
    
      
                
    
            
    

    
    
    pygame.draw.rect(screen, BLACK, [271, 245, 168, 154],6)
    pygame.draw.rect(screen, GREY, [440, 235, 15, 169])
    pygame.draw.rect(screen, GREY, [255, 236, 15, 167])



    knob()
    knob2()
    
    stars = []
  
    for i in range(200,400):
        x = random.randrange(274,434)
        y = random.randrange(255, 380)
        r = random.randrange(1,5)
        s = [ x,y,r,r,]
        
        stars.append(s)
        
       
    #pygame.draw.line(screen, GREEN, [300, 40], [100,500], 5)
   # pygame.draw.ellipse(screen, BLUE, [100, 100, 600, 300])
    #pygame.draw.polygon(screen, BLACK, [[200, 200], [50,400], [600, 500]], 10)
   
    
    
    #for s in stars:
        # pygame.draw.ellipse(screen,GREEN,s)




    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    #pygame.draw.arc(screen, ORANGE, [100, 100, 100, 100], 0, math.pi/2, 1)
    #pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi/2, 50)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
