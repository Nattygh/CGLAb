# B) On your canvas above, draw a red line that has a width of 3 & a 
# length of 200 pixels. Let the point of origin (or the start position) 
# be (50, 50).                              


import pygame

def draw_red_line():
    pygame.init()
    screen = pygame.display.set_mode((500, 400))
    screen.fill((255, 255, 255)) 
    pygame.draw.line(screen, (255, 0, 0), (50, 50), (250, 50), 3)
    pygame.display.flip()

    pygame.time.wait(3000)
    pygame.quit()

draw_red_line()
