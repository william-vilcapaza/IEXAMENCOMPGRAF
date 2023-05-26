# Usando libreria pygame para realizar el triangulo Sierpinski
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

# Función para dibujar el triángulo de Sierpinski
def draw_sierpinski(x, y, size, depth):
    if depth == 0:
        glBegin(GL_TRIANGLES)
        glVertex2f(x, y)
        glVertex2f(x + size, y)
        glVertex2f(x + size / 2, y + size)
        glEnd()
    else:
        draw_sierpinski(x, y, size / 2, depth - 1)
        draw_sierpinski(x + size / 2, y, size / 2, depth - 1)
        draw_sierpinski(x + size / 4, y + size / 2, size / 2, depth - 1)

# Función para dibujar la escena
def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    draw_sierpinski(-0.5, -0.5, 1.0, 5)

    pygame.display.flip()

# Configuración inicial de Pygame
pygame.init()
width, height = 800, 800
pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

# Configuración inicial de OpenGL
glViewport(0, 0, width, height)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
aspect_ratio = width / height
glOrtho(-aspect_ratio, aspect_ratio, -1, 1, -1, 1)
glMatrixMode(GL_MODELVIEW)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_scene()

# Finalización del programa
pygame.quit()