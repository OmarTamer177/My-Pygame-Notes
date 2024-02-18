#################################################################
# Rectangles
#->Precise positioning of surfaces
#->Basic collisions
# 
# -Surface for image information
# -Placement is via rectangles
# ---sprite class combines both---
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

#To Create a rectangle around a player:
#1-Create the player surface and blit in on screen
player = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
#2-create the rectangle by 2 ways:
#2.2-pygame.Rect(left, top, width, height) function, creating a rectangle 
#specifying the size and coordinates
#2.2-surface.get_rect(position = (x,y)) function, which sets the coordinates 
#and gets the size of the surface and placing it inside a rectangle
player_rect = player.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    screen.fill('black')
    
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (30, 20))

    screen.blit(snail, snail_rect)
    if snail_rect.right>0:
        snail_rect.left -= 5
    else:
        snail_rect.left = 800

    #blit player on screen
    screen.blit(player, player_rect)
    #To move the player using the rectangle, 
    #alter the positions of the rectangle (left, right, topright...)
    if player_rect.left < 800:
        player_rect.left +=2
    else:
        player_rect.right = 0

    pygame.display.update()
    clock.tick(60)