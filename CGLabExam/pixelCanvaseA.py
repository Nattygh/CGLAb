# 4.(A)Draw a 500 by 400 pixel canvas using pygame. Make it in a 
# function named main. Set the title of your canvas. Add an event 
# to your canvas so that it quits when Key F1 is pressed in your 
# keyboard. Fill the canvas with white color.  

import pygame
from pygame.locals import QUIT, KEYDOWN, K_F1

def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 400))
    pygame.display.set_caption("My Canvas")
    screen.fill((255, 255, 255))  # White background
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_F1):
                running = False

    pygame.quit()

main()
