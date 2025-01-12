# 5. Write a Python code to draw a triangle, colored purple, using 
# PyGame and OpenGL.  

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

# Initialize PyGame
pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.DOUBLEBUF | pygame.OPENGL)
pygame.display.set_caption("Triangle with PyOpenGL")

# OpenGL Settings
glClearColor(1.0, 1.0, 1.0, 1.0)  # White background
glMatrixMode(GL_PROJECTION)
gluPerspective(45, (800 / 600), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5.0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear the screen

    # Draw a triangle
    glBegin(GL_TRIANGLES)
    glColor3f(0.5, 0, 0.5)  # Purple color
    glVertex3f(-1.0, -1.0, 0.0)  # Vertex 1
    glVertex3f(1.0, -1.0, 0.0)   # Vertex 2
    glVertex3f(0.0, 1.0, 0.0)    # Vertex 3
    glEnd()

    pygame.display.flip()  # Swap buffers
    pygame.time.wait(10)

pygame.quit()

