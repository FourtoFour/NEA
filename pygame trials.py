import pygame as pg
import time

#initiate
pg.init()

#set screen dimensions
scrn = pg.display.set_mode((500,500))

#title for program
pg.display.set_caption("pg_trials.py")


done = False



pg.draw.rect(scrn, (225,225,225), pg.Rect(30, 30, 60, 60))

#for player rect
x = 60
y = 60

#player movment speeds
mov_neg_y = 2000
mov_pos_y = 2000
mov_neg_x = 2000
mov_pos_x = 2000

#frame counter sort of?
clock = pg.time.Clock()

while not done:

    for event in pg.event.get():

        if event.type == pg.QUIT:

            done = True
    #boilerplate over
    clock.tick(2000)

    #registering key presses
    pressed = pg.key.get_pressed()
    if pressed[pg.K_UP]: y-= mov_neg_y
    if pressed[pg.K_DOWN]: y+= mov_pos_y
    if pressed[pg.K_LEFT]: x-= mov_neg_x
    if pressed[pg.K_RIGHT]: x+= mov_pos_x


    scrn.fill((0,0,0))
    
    #drawing boundaries
    bound_1 = pg.draw.rect(scrn, (225,225,225), pg.Rect(30, 30, 20, 450))
    bound_2 = pg.draw.rect(scrn, (225,225,225), pg.Rect(30, 30, 450, 20))
    bound_3 = pg.draw.rect(scrn, (225,225,225), pg.Rect(30, 460, 450, 20))
    bound_4 = pg.draw.rect(scrn, (225,225,225), pg.Rect(460, 30, 20, 450))

    
    #draw rectangle for player movement
    player_rect = pg.draw.rect(scrn, (0,128,225), pg.Rect(x,y, 90,90))
    

    #collisions between player and stationary boundaries
    collision_1 = bound_1.colliderect(player_rect)
    collision_2 = bound_2.colliderect(player_rect)
    collision_3 = bound_3.colliderect(player_rect)
    collision_4 = bound_4.colliderect(player_rect)
    if collision_1 == 1:
        print("collision_1 is hit")
    elif collision_2 == 1:
        print("collision_2 is hit")
    elif collision_3 == 1:
        print("collision_3 is hit")
    elif collision_4 == 1:
        print("collision_4 is hit")

    #denying collision moves

    #left barrier
    while collision_1 == 1:
        mov_neg_x = 0
        break
    else:
        mov_neg_x = 2

    #right barrier
    while collision_4 == 1:
        mov_pos_x = 0
        break
    else:
        mov_pos_x = 2

    #top barrier
    while collision_2 == 1:
        mov_neg_y = 0
        break
    else:
        mov_neg_y = 2

    #bottom barrier
    while collision_3 == 1:
        mov_pos_y = 0
        break
    else:
        mov_pos_y = 2

    
        
    
        

        

    


    #update display each frame
    pg.display.update()


pg.quit()

class car(pg.sprite.Sprite):
    def __init__(self, x, y):
        pass

    def x():
        print('asdasdas')

car.x()
        
    
    
