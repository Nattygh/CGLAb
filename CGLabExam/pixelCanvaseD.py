# D) Draw a point (make it purple) on the middle of the above 
# drawing. 

import pygame

def draw_purple_point():
    pygame.init()
    screen = pygame.display.set_mode((500, 400))
    screen.fill((255, 255, 255))  # White background
    pygame.draw.circle(screen, (128, 0, 128), (250, 100), 5)
    pygame.display.flip()

    pygame.time.wait(3000)
    pygame.quit()

# Run the function
draw_purple_point()
