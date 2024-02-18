#################################################################
# Displaying images (With surfaces)
# To display anything on the screen we need a surface
# |
# --> Display surface: The game window, anything displays here (only 1)
# --> (regular) surface: Essentially a single image 
#     (Something imported, rendered text or a plain color) (flexible amount)
#################################################################
import pygame, sys

pygame.init()

screen = pygame.display.set_mode((800, 400)) 
pygame.display.set_caption('Game Title')
clock = pygame.time.Clock()

#Creating a (regular) surface
#Surface( (Width, Height) ) takes a tuple for the surface size
test_surface = pygame.Surface((100, 200))
#filling the surface with color either by: 
#naming a color 
#or passing an RGB tuple(Red, Green, Blue) 
#or by hex-color #rrggbb
test_surface.fill('red')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    

    #attach the test surface to the display surface
    #using .blit(Surface, position as tuple of x and y) function in the display surface methods
    #the position is set from the top left of the surface relative to the origin point(0,0) 
    #at the top left of the display surface
    # ---> x+
    # |
    # v y+
    #blit = block image transfer
    screen.blit(test_surface, (200,100))

    pygame.display.update()
    clock.tick(60)