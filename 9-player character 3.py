#################################################################
# The player character 2: creating floor
# check the y-position of the player if it is below the floor
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
player_gravity = 0
#To solve the problem of constantly jumping, we need a player jumping variable 
#to indicate whether the player is jumping or not, and setting the variable to true while jumping
player_jumping = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not player_jumping:
                player_gravity = -18
                player_jumping = True

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

    player_rect.y += player_gravity
    #Creating a floor is by setting a boundary(which is the floor) the player can't fall under
    #if the player passes the floor; clear gravity and place the player on the floor
    if player_rect.bottom > 300: 
        player_gravity = 0
        player_rect.bottom = 300
        player_jumping = False
    else:
        player_gravity += 1

    screen.blit(player, player_rect)
    pygame.display.update()
    clock.tick(60)