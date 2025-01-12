# C) Use draw.polygon or just use vertices to draw triangles and 
# write a code that displays a shape as shown below: 
 
import pygame

def draw_triangle():
    pygame.init()
    screen = pygame.display.set_mode((500, 400))
    screen.fill((255, 255, 255))  # White background
    pygame.draw.polygon(screen, (0, 0, 255), [(250, 50), (300, 150), (200, 150)], 0)
    pygame.display.flip()

    pygame.time.wait(3000)
    pygame.quit()

# Run the function
draw_triangle()
