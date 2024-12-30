
import random
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

Xpos = 400
Ypos = 660

enemyYpos = 0
char = pygame.Rect((Xpos,Ypos,100,20))
enemy = pygame.Rect((random.randint(100, 1200), enemyYpos, 30, 30))

while running:

    # A W D S keys input
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        char.move_ip(-10, 0)

    key = pygame.key.get_pressed()
    if key[pygame.K_d] == True:
        char.move_ip(+10, 0)
    
    if enemyYpos != 720:
        enemy.move_ip(0,+3)


    #ARROW KEY INPUT
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] == True:
        char.move_ip(-10, 0)

    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT] == True:
        char.move_ip(+10, 0)
    
    if enemyYpos != 720:
        enemy.move_ip(0,+5)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    screen.fill("black")
    pygame.draw.rect(screen, (0,255,0), char)
    pygame.draw.rect(screen, (255,0,0), enemy)
    clock.tick(60)  



pygame.quit()