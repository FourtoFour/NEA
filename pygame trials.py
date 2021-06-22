import pygame

pygame.init()

scrn = pygame.display.set_mode((500,500))

#title for program
pygame.display.set_caption("pygame_trials.py")

done = False



pygame.draw.rect(scrn, (225,225,225), pygame.Rect(30, 30, 60, 60))

x = 60
y = 60

clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            done = True
    #boilerplate over
    clock.tick(60)
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y-= 1
    if pressed[pygame.K_DOWN]: y+= 1
    if pressed[pygame.K_LEFT]: x-= 1
    if pressed[pygame.K_RIGHT]: x+= 1


    scrn.fill((0,0,0))
    
    #drawing boundaries
    pygame.draw.rect(scrn, (225,225,225), pygame.Rect(30, 30, 20, 450))
    pygame.draw.rect(scrn, (225,225,225), pygame.Rect(30, 30, 450, 20))
    pygame.draw.rect(scrn, (225,225,225), pygame.Rect(30, 460, 450, 20))
    pygame.draw.rect(scrn, (225,225,225), pygame.Rect(460, 30, 20, 450))

    
    #draw rectangle for player movement
    pygame.draw.rect(scrn, (0,128,225), pygame.Rect(x,y, 90,90))

    
    #update display each frame
    pygame.display.update()


pygame.quit()
    
