# Imports
import pygame
import random

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
GREEN = (100, 255, 100)

# Images
ship_img = pygame.image.load('images/p1backp.png')
enemy = pygame.image.load('images/p1fronty.png')
laser_img = pygame.image.load('images/bullet.png')
field = pygame.image.load("images/footballfield.png")
bomb_img  = pygame.image.load("images/anvil.jpg")
enemy_img = pygame.image.load('images/p1back.png')


# Game classes
class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.speed = 3
        self.shield = 10

    def move_left(self):
        self.rect.x -= self.speed
        
    def move_right(self):
        self.rect.x += self.speed

    def shoot(self):
        laser = Laser(laser_img)
        laser.rect.centerx = self.rect.centerx
        laser.rect.centery = self.rect.top
        lasers.add(laser)

    def update(self, bombs):
        hit_list = pygame.sprite.spritecollide(self, bombs, True)

        for hit in hit_list:
            #OOF.play()
            self.shield -= 1

        if self.shield == 0:
            #EXPLOSION.play()
            self.kill()
    
class Laser(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        
        self.speed = 5

    def update(self):
        self.rect.y -= self.speed
    
class Mob(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def drop_bomb(self):
        bomb = Bomb(bomb_img)
        bomb.rect.centerx = self.rect.centerx
        bomb.rect.centery = self.rect.bottom
        bombs.add(bomb)
        

    def update(self, lasers):
        hit_list = pygame.sprite.spritecollide(self, lasers, True)

        if len(hit_list) > 0:
           # EXPLOSION.play()
            self.kill()



class Bomb(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        
        self.speed = 3

    def update(self):
        self.rect.y += self.speed
    
    
class Fleet:

    def __init__(self, mobs):
        self.mobs = mobs
        self.bomb_rate = 60

        self.speed = 3
        self.moving_right = True
        
    def move(self):
    
        reverse = False

        if self.moving_right:
            for e in enemy:
                e.rect.x += self.speed
                if e.rect.right >= WIDTH:
                    reverse = True

                    
        else:
            for e in enemy:
                e.rect.x -= self.speed
                if e.rect.left <= 0:
                    reverse = True

           
                

        if reverse:  
            self.moving_right = not self.moving_right
            
            for e in enemy:
                e.rect.y += 10
                
            for m in mobs:
                m.rect.y += 20
            

    

    def choose_bomber(self):
        rand = random.randrange(0, self.bomb_rate)
        all_mobs = mobs.sprites()
        
        if len(all_mobs) > 0 and rand == 0:
            return random.choice(all_mobs)
        else:
            return None
    
    def update(self):
        self.move()

        bomber = self.choose_bomber()
        if bomber != None:
            bomber.drop_bomb()

    
# Make game objects
ship = Ship(384, 536, ship_img)
mob1 = Mob (123,64,enemy)
mob2 = Mob (256,64,enemy)
mob3 = Mob (364,64,enemy)


enemy1 = Mob (123,164,enemy_img)
enemy2 = Mob (256,164,enemy_img)
enemy3 = Mob (364,164,enemy_img)

# Make sprite groups
player = pygame.sprite.GroupSingle()
player.add(ship)

lasers = pygame.sprite.Group()
mobs = pygame.sprite.Group()
mobs.add(mob1,mob2,mob3)

enemy  = pygame.sprite.Group()
enemy.add(enemy1,enemy2,enemy3)

bombs = pygame.sprite.Group()

# Make fleet
fleet = Fleet(mobs)


# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ship.shoot()

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]:
        ship.move_left()
    elif pressed[pygame.K_RIGHT]:
        ship.move_right()
        
    
    # Game logic (Check for collisions, update points, etc.)
   
    player.update(bombs)
    lasers.update()
    bombs.update()
    mobs.update(lasers)
    fleet.update()
    
        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.blit(field,(0,0))
    lasers.draw(screen)
    bombs.draw(screen)
    player.draw(screen)
    mobs.draw(screen)
    enemy.draw(screen)


    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
