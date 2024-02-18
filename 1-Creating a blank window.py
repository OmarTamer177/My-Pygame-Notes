##################################################
# creating a basic blank window
##################################################
import pygame, sys

#starts pygame and initiates all sub-parts of pygame
pygame.init()

#Creating the display surface and displaying it
screen = pygame.display.set_mode((800, 400)) #set_mode( (Width, Height) ) takes a tuple of the window size

#Setting the title for the game at the top of the window
pygame.display.set_caption('Game Title')

#creating a clock objects which helps controlling the Frame Rate
clock = pygame.time.Clock()

#Game-Loop that runs forever 
#which draws all elements
#and updates everything
while True:
    
    #Event-Loop That checks for all player inputs
    for event in pygame.event.get():
        #if the player chose to close the window through the X button at the top right
        if event.type == pygame.QUIT:
            #closes pygame
            #quit() is the opposite of init()
            pygame.quit()
            #ends the code
            sys.exit()
    
    #Updates display surfaces    
    pygame.display.update()

    #Caps the framerate at 60 fps
    #basically capping the gameloop to run only 60 times per second 
    clock.tick(60)