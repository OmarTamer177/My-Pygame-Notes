#################################################################
# Drawing with rectangles
# This is done by using pygame.draw module
# which is also used to draw circles, lines, points, elipses...
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

    screen.fill('black')
    
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    #To draw a rectangle, 
    #pygame.draw.rect(display_surface, color, rectangle, width = 0, border_radius = 0) is used
    #width argument is width of the border around the rectangle
    pygame.draw.rect(screen, '#c0e8ec' , score_rect)
    #used just for drawing a border around the main rectangle 
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)

    #To draw a line,
    #pygame.draw.line(display_surface, color, start_pos, end_pos, width = 1)
    #or pygame.draw.aaline(..), aa stands for anti-aliasing
    #pygame.draw.line(screen,'gold', (0, 0), (screen.get_width(),screen.get_height()), 6)

    #to make a ray following the mouse:
    #pygame.draw.line(screen,'gold', (0, 0), pygame.mouse.get_pos(), 6)

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
    
    if player_rect.colliderect(snail_rect):
        print('Collision!')
    
    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        print('collidepoint!!')

    pygame.display.update()
    clock.tick(60)