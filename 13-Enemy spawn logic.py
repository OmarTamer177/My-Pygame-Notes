#################################################################
# Enemy spawn logic using Timers(spawning multiple obstacles)
#################################################################
import pygame, sys

pygame.init()

pygame.display.set_caption('Game Title')
screen = pygame.display.set_mode((800, 400)) 
clock = pygame.time.Clock()

game_active = False

sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()

font = pygame.font.Font('font/Pixeltype.ttf', 50)

score = 0
start_time = 0

score_surface = font.render("score: " + str(score), False, (64, 64, 64))
score_rect = score_surface.get_rect(center = (400,20))

snail = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail.get_rect(bottomright = (800,300))

player = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player.get_rect(midbottom = (80,300))
player_gravity = 0
player_jumping = False

stand_player = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
stand_player = pygame.transform.rotozoom(stand_player, 0, 1.5)

stand_player_rect = stand_player.get_rect(center = (400, 200))

intro_text = font.render("Snail Hopper", False, 'black')
intro_text_rect = intro_text.get_rect(center = (400, 50))

instruction_text = font.render("Press any button to start", False, 'black')
instruction_text_rect = instruction_text.get_rect(center = (410, 350))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not player_jumping:
                    player_gravity = -18
                    player_jumping = True
        else:
            if event.type == pygame.KEYDOWN:
                game_active = True

    if game_active:
        screen.fill('black')
        
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        
        pygame.draw.rect(screen, '#c0e8ec' , score_rect)
        pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)

        curr_time = pygame.time.get_ticks() - start_time
        score = int(curr_time / 1000)

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

        if player_rect.colliderect(snail_rect):
            game_active = False
        
        if not game_active:
            print("game over")

        screen.blit(player, player_rect)
    else:
        screen.fill((94, 129, 162))
        
        score_text = font.render(f'score: {score}', False, 'black')
        score_text_rect = score_text.get_rect(center = (400, 340))
        
        screen.blit(stand_player, stand_player_rect)
        screen.blit(intro_text, intro_text_rect)
        if not score:
            screen.blit(instruction_text, instruction_text_rect)
        else:
            screen.blit(score_text, score_text_rect)

        snail_rect.right = 800
        player_rect.y = 300
        start_time = pygame.time.get_ticks()

    pygame.display.update()
    clock.tick(60)