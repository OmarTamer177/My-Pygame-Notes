#################################################################
# Enemy spawn logic using Timers(spawning multiple obstacles)
# We create a custom user event 
# that is triggered in certain time interval
#################################################################
import pygame, sys, random

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
#score_rect = score_surface.get_rect(center = (400,20))
score_rect = pygame.Rect(400 - (score_surface.get_width()/2), 10, 
                         score_surface.get_width() + 20, score_surface.get_height())

#adding a new enemy type which is the fly
snail = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
fly = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()

#To create obstacles logic:
#1.create a list of obstacle rectangles
#2.everytime the timer ticks, we add a rectangle
#3.we move each rectangle to the left for every frame
#4.delete rectangles too far left
obstacles = []

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

#To create a timer we:
#1.Create a custom event
#2.Tell pygame to continuously trigger that event providing a time frame
#3.add code to event loop
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1200)

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
        if event.type == obstacle_timer and game_active:
            #randomly generate an obstacle whether a snail or fly
            if random.randint(0,2):
                new_obs = snail.get_rect(bottomright = (random.randint(900, 1100), 300))
            else:
                new_obs = fly.get_rect(bottomright = (random.randint(900, 1100), 300 - player_rect.height - 10))
            obstacles.append(new_obs)

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
        print(player_gravity)
        player_gravity = 0
        start_time = pygame.time.get_ticks()

    pygame.display.update()
    clock.tick(60)