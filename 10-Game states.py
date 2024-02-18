#################################################################
# Creating different game states
# 1.Game over state
#################################################################
import pygame, sys

pygame.init()

pygame.display.set_caption('Game Title')
screen = pygame.display.set_mode((800, 400)) 
clock = pygame.time.Clock()

#To create the gameover state we need a variable indicating whether the game is still active
game_active = True

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
player_jumping = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #if game is over wait for player input to reset the game
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not player_jumping:
                    player_gravity = -18
                    player_jumping = True
        else:
            if event.type == pygame.KEYDOWN:
                game_active = True
    #if game is still active continue game normally
    if game_active:
        screen.fill('black')
        
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        
        pygame.draw.rect(screen, '#c0e8ec' , score_rect)
        pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)

        score_surface = font.render("score: " + str(score), False, (64, 64, 64))
        screen.blit(score_surface, score_rect)

        screen.blit(snail, snail_rect)
        if snail_rect.right>0:
            snail_rect.left -= 5
        else:
            snail_rect.left = 800

        player_rect.y += player_gravity
        if player_rect.bottom > 300: 
            player_gravity = 0
            player_rect.bottom = 300
            player_jumping = False
        else:
            player_gravity += 1

        #Gameover state happens when the snail touches the player
        if player_rect.colliderect(snail_rect):
            game_active = False
        
        #Create a condition checking if the state of the game
        if not game_active:
            print("game over")

        screen.blit(player, player_rect)

    #if game is over, check for player input to start over
    else:
        snail_rect.right = 800
        player_rect.y = 300

    pygame.display.update()
    clock.tick(60)