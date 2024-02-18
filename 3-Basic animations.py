#################################################################
# Basic animations
#################################################################
import pygame, sys

pygame.init()

screen = pygame.display.set_mode((800, 400)) 
pygame.display.set_caption('Game Title')
clock = pygame.time.Clock()

#by adding .convert_alpha(), 
#images converts to be better used by pygame by removing alpha values
sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()

font = pygame.font.Font('font/Pixeltype.ttf', 50)
score = 0
text_surface = font.render("score: " + str(score), False, 'black')

#To make a snail move from the left to the right we need to:
# 1-create the snail surface
# 2-blit it on screen
snail = pygame.image.load('graphics/snail/snail1.png').convert_alpha()

# 3-create a variable represeting the position of the snail 
#   that changes over time to emulate the movement
snail_x_pos = 800 - snail.get_width()

# 4-constantly change the value of snail_x_pos value in the gameloop to move the snail
#(put the proper condition for the change)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    

    #clear the screen entirely before redrawing and updating elements
    #to get rid of any mistakes that could happen
    #by filling the screen with black
    screen.fill('black')
    
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (30, 20))

    #blit snail on screen
    screen.blit(snail, (snail_x_pos, 300 - snail.get_height()))

    #change the value of snail_x_pos with the proper condition
    #return the snail to the start of the scene when it reaches the end
    if snail_x_pos > -snail.get_width():
        snail_x_pos -= 5
    else:
        snail_x_pos = 800

    pygame.display.update()
    clock.tick(60)