#################################################################
# Collisions
#################################################################
import pygame, sys

pygame.init()

pygame.display.set_caption('Game Title')
screen = pygame.display.set_mode((800, 400)) 
clock = pygame.time.Clock()

sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()

font = pygame.font.Font('font/Pixeltype.ttf', 50)
score = 0
text_surface = font.render("score: " + str(score), False, 'black')

snail = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail.get_rect(bottomright = (800,300))

player = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #checks if the mouse collides with the player rectangle
        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos):
                print('collision from eventloop!!')
        #checks the position of the mouse
        if event.type == pygame.MOUSEMOTION: pass
        #checkes if a mouse button is pressed
        if event.type == pygame.MOUSEBUTTONDOWN: pass
        #checks if mouse button is released
        if event.type == pygame.MOUSEBUTTONUP: pass

    screen.fill('black')
    
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (30, 20))

    screen.blit(snail, snail_rect)
    if snail_rect.right>0:
        snail_rect.left -= 5
    else:
        snail_rect.left = 800

    screen.blit(player, player_rect)
    if player_rect.left < 800:
        player_rect.left +=2
    else:
        player_rect.right = 0
    
    #To check for collision between 2 objects, we use rect1.colliderect(rect2) 
    #which returns 0 if no collision and 1 if there is collision
    if player_rect.colliderect(snail_rect):
        #code for what happen if the objects collide
        print('Collision!') #dummy code
    
    #rect.collidepoint((x,y)) funtion checks if the rectangle collides with a certain point
    #useful if using mouse controls
    #to get the mouse position, either in the eventloop or by using pygame.mouse.get_pos()
    #pygame.mouse gives information about mouse position and with buttons are being pressed
    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        print('collidepoint!!')

    pygame.display.update()
    clock.tick(60)