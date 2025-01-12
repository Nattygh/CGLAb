# 6) Write a Python function that takes two points P1(x1, y1) and 
# P2(x2, y2) to draw a line thru P1 and P2 using PyGame and 
# OpenGL.  
# HINT: Use GL_LINES, glVertex2f and glColor3f 
# Syntax: 
# def draw_line(x1, y1, x2, y2): 
# glBegin(….) 
# //your code here 
# glEnd() 

import pygame
from pygame.locals import *

pygame.init()

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_line(x1, y1, x2, y2):
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)  # Red color
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Line Example")
    glClearColor(1, 1, 1, 1)
    glutDisplayFunc(lambda: draw_line(-0.5, -0.5, 0.5, 0.5))
    glutMainLoop()

# Run the function
main()

