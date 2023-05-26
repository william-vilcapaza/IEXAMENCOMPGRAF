import pygame
import random

# Inicializar pygame
pygame.init()
WIDTH = 800
HEIGHT = 600

# Color que se va a utilizar para los cubos 
CELESTE = (70, 205, 255)

# Clase para el cubo
class Cube:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(1, 5) #velocidad del cubo aleatorio

    def update(self): #actualizar la velocidad
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, CELESTE, (self.x, self.y, 50, 50))

# Crear la pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cubos cayendo")

#Cubos
cubes = []

# Crear exactamente 50 cubos
while len(cubes) < 50:
    x = random.randint(0, WIDTH - 50)
    y = random.randint(-200, -50)
    cube = Cube(x, y)
    cubes.append(cube)

# Bucle principal del juego
running = True
clock = pygame.time.Clock()

while running:
    # Para controlar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar y dibujar los cubos
    screen.fill((0, 0, 0))
    for cube in cubes:
        cube.update()
        cube.draw(screen)

    # Eliminar los cubos que salen de la pantalla
    cubes = [cube for cube in cubes if cube.y < HEIGHT]

    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(60)

# Salir del juego
pygame.quit()