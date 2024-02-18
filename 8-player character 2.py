#################################################################
# The player character 2: jumping & gravity
# gravity: the longer you fall, the faster you fall(acceleration)
# falling_velocity = gravity.time
# however, fun or ease > accurate physics
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
#Initializing a gravity variable that will then be increased while falling
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos):
                player_gravity = -20
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #implementing the actual jump function
                player_gravity = -20


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
    #linking gravity with player targeting vertical attribute
    #increasing the velocity of falling as time passes 
    player_rect.y += player_gravity
    #increasing gravity after each cycle
    player_gravity += 1

    pygame.display.update()
    clock.tick(60)