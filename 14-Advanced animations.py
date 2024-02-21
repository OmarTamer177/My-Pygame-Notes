#################################################################
# Advanced animations
# adding animation for player, snail and fly
# animation: place a slightly different looking images 
# in rapid succession
#################################################################
import pygame, sys, random

pygame.init()

def player_animation():
    #display walking animation when player is on ground
    #display jumping animation when player is not on ground
    global player, player_index
    if player_jumping:
        player = player_jump
    else:
        player_index += 0.1
        if player_index > len(player_walk): 
            player_index = 0
        player = player_walk[int(player_index)]

def snail_animation():
    pass

def fly_animation():
    pass


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
score_rect = pygame.Rect(400 - (score_surface.get_width()/2), 10, 
                         score_surface.get_width() + 20, score_surface.get_height())

snail_frames = [pygame.image.load('graphics/snail/snail1.png').convert_alpha(), 
         pygame.image.load('graphics/snail/snail2.png').convert_alpha()]
snail_index = 0
snail = snail_frames[0]

fly_frames = [pygame.image.load('graphics/Fly/Fly1.png').convert_alpha(),
         pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()]
fly_index = 0
fly = fly_frames[0]

obstacles = []

#To make player animation: we create a timer that updates the surface
player_walk = [pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha(), 
               pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()]
player_index = 0
player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()

player = player_walk[0]
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

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1200)

#To make obstacles animation: we rely on the inbuild timers/ 
#                             to update all obstacle surfaces
snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 200)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 50)

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

        #only if the game is active, trigger obstacles and add a new obstacle to the list
        if game_active:
            if event.type == obstacle_timer and game_active:
                #randomly generate an obstacle whether a snail or fly
                if random.randint(0,2):
                    new_obs = snail.get_rect(bottomright = (random.randint(900, 1100), 300))
                else:
                    new_obs = fly.get_rect(bottomright = (random.randint(900, 1100), 300 - player_rect.height - 10))
                obstacles.append(new_obs)
            
            #Execute the timer for the snail animation
            if event.type == snail_animation_timer:
                snail = snail_frames[snail_index]
                if snail_index:
                    snail_index = 0
                else: 
                    snail_index = 1

            #Execute the timer for the fly animation
            if event.type == fly_animation_timer:
                fly = fly_frames[fly_index]
                if fly_index:
                    fly_index = 0
                else: 
                    fly_index = 1

    if game_active:
        screen.fill('black')
        
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        
        pygame.draw.rect(screen, '#c0e8ec' , score_rect)
        pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)

        curr_time = pygame.time.get_ticks() - start_time
        score = int(curr_time / 1000)

        score_surface = font.render("score: " + str(score), False, (64, 64, 64))
        screen.blit(score_surface, (score_rect.x + 10, score_rect.y + 4))

        player_rect.y += player_gravity
        if player_rect.bottom > 300: 
            player_gravity = 0
            player_rect.bottom = 300
            player_jumping = False
        else:
            player_gravity += 1

        #if obstacles list isn't empty
        if obstacles:
            #itirate over obstacles list for:
            for i in range(0,len(obstacles) - 1):
                #update the position of snails and blit them on screen
                obstacles[i].x -= 6
                #check whether the obstacle is a snail or fly 
                if obstacles[i].bottom == 300:
                    screen.blit(snail, obstacles[i])
                else:
                    screen.blit(fly, obstacles[i])

                #Update the game over condition
                if player_rect.colliderect(obstacles[i]):
                    game_active = False
            #remove any obstacles outside the screen
            obstacles = [obstacle for obstacle in obstacles if obstacle.x > -100]
        
        player_animation()
        screen.blit(player, player_rect)
    else:
        screen.fill((94, 129, 162))
        
        score_text = font.render(f'score: {score}', False, 'black')
        score_text_rect = score_text.get_rect(center = (400, 340))

        game_over_text = font.render('Game Over', False, 'black')
        game_over_text_rect = score_text.get_rect(center = (390, 50))
        
        screen.blit(stand_player, stand_player_rect)
        if not score:
            screen.blit(instruction_text, instruction_text_rect)
            screen.blit(intro_text, intro_text_rect)
        else:
            screen.blit(game_over_text, game_over_text_rect)
            screen.blit(score_text, score_text_rect)

        obstacles = []
        player_rect.y = 300
        player_gravity = 0
        start_time = pygame.time.get_ticks()

    pygame.display.update()
    clock.tick(60)