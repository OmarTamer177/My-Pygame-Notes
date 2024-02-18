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

#Creating (regular) surfaces of the sky and ground and loading an image
#by displaying the sky and ground, we have a scene!
sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')

#To create a font
#-->Create an image of the text
#-->place it on the display surface
# 1-create a font (size and style) => pygame.font.Font(font_style, font_size)
test_font = pygame.font.Font('font/Pixeltype.ttf', 50) #None -> default font, for other font specify a file path
# 2-write it on a surface => .render(text to be displayed, Anti-aliasing (smooth surfaces)(NOT good for pixel-art), color)
text_surface = test_font.render("score", False, 'black')
# 3-blit it on screen

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    

    #attach the sky and ground surfaces to the display surface
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    #blit text on screen
    screen.blit(text_surface, (30, 20))

    pygame.display.update()
    clock.tick(60)