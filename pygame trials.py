import pygame as pg
import time

#not using tkinter as it causes crashes

#initiate
pg.init()

#set screen dimensions
scrn = pg.display.set_mode((500,500))

#title for program
pg.display.set_caption("pg_trials.py")

#background for game
bg = pg.image.load("stonensand.png")

#idk what this does
done = False

pg.draw.rect(scrn, (225,225,225), pg.Rect(30, 30, 60, 60))

#test_text
yellow = (255, 255, 0)

m_font = pg.font.SysFont("Comic Sans MS", 30)

label_seen = m_font.render("Text example!", 1, yellow)

scrn.blit(label_seen, (100, 100))

#for player rect
x = 60
y = 60

#player movment speeds
in_mov_neg_y , mov_neg_y = 1,1
in_mov_pos_y , mov_pos_y = 1,1
in_mov_neg_x , mov_neg_x = 1,1
in_mov_pos_x , mov_pos_x = 1,1

#frame counter sort of?
clock = pg.time.Clock()

while not done:

    for event in pg.event.get():

        if event.type == pg.QUIT:

            done = True
    


    #boilerplate over
    clock.tick(200)

    #registering key presses
    pressed = pg.key.get_pressed()
    if pressed[pg.K_UP]:
        y-= mov_neg_y and in_mov_neg_y
    if pressed[pg.K_DOWN]:
        y+= mov_pos_y and in_mov_pos_y
    if pressed[pg.K_LEFT]:
        x-= mov_neg_x and in_mov_neg_x
    if pressed[pg.K_RIGHT]:
        x+= mov_pos_x and in_mov_pos_x

    #this code below was causing bg not to load
    #scrn.fill((0,0,0))
    scrn.blit(bg,(0,0))

    
    #drawing boundaries
    bound_1 = pg.draw.rect(scrn, (225,225,225), pg.Rect(30, 30, 20, 450))
    bound_2 = pg.draw.rect(scrn, (225,225,225), pg.Rect(30, 30, 450, 20))
    bound_3 = pg.draw.rect(scrn, (225,225,225), pg.Rect(30, 460, 450, 20))
    bound_4 = pg.draw.rect(scrn, (225,225,225), pg.Rect(460, 30, 20, 450))
    #middle boundaries
    bound_5 = pg.draw.rect(scrn, (225,225,225), pg.Rect(165, 150, 20, 150))
    bound_6 = pg.draw.rect(scrn, (225,225,225), pg.Rect(175, 150, 150, 20))
    bound_7 = pg.draw.rect(scrn, (225,225,225), pg.Rect(165, 300, 180, 20))
    bound_8 = pg.draw.rect(scrn, (225,225,225), pg.Rect(325, 150, 20, 150))
    #lap boundary
    bound_9 = pg.draw.rect(scrn, (225,225,225), pg.Rect(345, 150, 125, 20))
    

    
    #draw rectangle for player movement
    player_rect = pg.draw.rect(scrn, (0,128,225), pg.Rect(x,y, 20,20))

    #collisions between player and stationary boundaries
    collision_1 = bound_1.colliderect(player_rect)
    collision_2 = bound_2.colliderect(player_rect)
    collision_3 = bound_3.colliderect(player_rect)
    collision_4 = bound_4.colliderect(player_rect)
    collision_5 = bound_5.colliderect(player_rect)
    collision_6 = bound_6.colliderect(player_rect)
    collision_7 = bound_7.colliderect(player_rect)
    collision_8 = bound_8.colliderect(player_rect)
    collision_9 = bound_9.colliderect(player_rect)
    
    if collision_1 == 1:
        print("collision_1 is hit")
    elif collision_2 == 1:
        print("collision_2 is hit")
    elif collision_3 == 1:
        print("collision_3 is hit")
    elif collision_4 == 1:
        print("collision_4 is hit")
    elif collision_5 == 1:
        print("collision_5 is hit")
    elif collision_6 == 1:
        print("collision_6 is hit")
    elif collision_7 == 1:
        print("collision_7 is hit")
    elif collision_8 == 1:
        print("collision_8 is hit")
    elif collision_9 == 1:
        print("collision_9 is hit")
    #denying collision moves

    #left barrier
    while collision_1 == 1:
        mov_neg_x = 0
        break
    else:
        mov_neg_x = 1

    #right barrier
    while collision_4 == 1:
        mov_pos_x = 0
        break
    else:
        mov_pos_x = 1

    #top barrier
    while collision_2 == 1:
        mov_neg_y = 0
        break
    else:
        mov_neg_y = 1

    #bottom barrier
    while collision_3 == 1:
        mov_pos_y = 0
        break
    else:
        mov_pos_y = 1

    #inner barriers
    '''Inner barriers'''

    #top in barrier
    while collision_6 == 1:
        in_mov_pos_y = 0
        break
    else:
        in_mov_pos_y = 1

    #right in barrier
    while collision_8 == 1:
        in_mov_neg_x = 0
        break
    else:
        in_mov_neg_x = 1

    #left in barrier
    while collision_5 == 1:
        in_mov_pos_x = 0
        break
    else:
        in_mov_pos_x = 1

    #bottom in barrier
    while collision_7 == 1:
        in_mov_neg_y = 0
        break
    else:
        in_mov_neg_y = 1

    #----Collisions Over-----#
    
    
        
    
        

    #update display each frame
    scrn.blit(label_seen, (250, 0))
    pg.display.update()


pg.quit()

class car(pg.sprite.Sprite):
    def __init__(self, x, y):
        pass

    def x():
        print('asdasdas')

car.x()
        
    
    
