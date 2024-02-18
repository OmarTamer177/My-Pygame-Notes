#################################################################
# The player character 1: Keyboard input
# To check for keyboard input either by:
# 1-using sub-module pygame.key
# 2-the eventloop
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
score_surface = font.render("score: " + str(score), False, (64, 64, 64))
score_rect = score_surface.get_rect(center = (400,20))

snail = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail.get_rect(bottomright = (800,300))

player = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #To handle pressing keys in the eventloop:
        #1-check if any button is being pressed or released
        if event.type == pygame.KEYDOWN:
        #2-work with a specific key
            if event.key == pygame.K_SPACE:
                print('space!')


    screen.fill('black')
    
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    
    pygame.draw.rect(screen, '#c0e8ec' , score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)

    screen.blit(score_surface, score_rect)

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

    #pygame.key.get_pressed() is a function that 
    #returns a dictionary of the state of each keyboard key(is pressed or not)
    keys = pygame.key.get_pressed()

    #if the space is pressed, handle the jump action
    #if keys[pygame.K_SPACE]: 
    #    print('jump') #dummy code for jump

    pygame.display.update()
    clock.tick(60)