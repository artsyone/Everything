# Imports
import pygame

# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Space War"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# sounds


#images
bullet = pygame.image.load("images/bullet.png")
field = pygame.image.load("images/footballfield.png")
p1 = pygame.image.load("images/p1back.png")


# Game classes
class Ship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 32
        self.h = 32
        self.speed = 3
        self.shield = 10

    def move_left(self):
        self.x -= self.speed
        
    def move_right(self):
        self.x += self.speed

    def shoot(self):
        
        x = self.x + self.w/2 - 2 
        y = self.y
        las = Laser(x,y)
        lasers.append(las)
        print("Pew!")

    def update(self):
        pass

    def draw(self):
        rect = [self.x, self.y, self.w, self.h]
        screen.blit(p1,( rect))
    
class Laser:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 4
        self.h = 8
        self.speed = 6
      

    def update(self):
        self.y -= self.speed

    def draw(self):
        rect = [self.x, self.y, self.w, self.h]
        screen.blit(bullet ,(rect))

    
class Mob:

    def __init__(self):
        pass

    def update(self):
        pass


class Bomb:
    
    def __init__(self):
        pass

    def update(self):
        pass
    
    
class Fleet:

    def __init__(self):
        pass

    def update(self):
        pass

    
# Make game objects
player = Ship(384, 536)
lasers = []

# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]:
        player.move_left()
    elif pressed[pygame.K_RIGHT]:
        player.move_right()
        
    
    # Game logic (Check for collisions, update points, etc.)
    
    for las in lasers:
        las.update()
        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)
    screen.blit(field,(0,0))
    player.draw()

    for las in lasers:
        las.draw()
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
