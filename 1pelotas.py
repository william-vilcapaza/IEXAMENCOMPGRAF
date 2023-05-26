import pygame
import random

# Inicializando pygame para utilizarlo en el proyecto
pygame.init()
WIDTH = 500
HEIGHT = 300

# Colores que se van a utilizar
BLACK = (0, 0, 0)
CELESTE = (70, 205, 255)

# Clase pelota
class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius #se define el radio
        self.speed_x = random.randint(1, 3) #velocidad aleatoria entre 1 y 3 en x
        self.speed_y = random.randint(1, 3) #velocidad aleatoria entre 1 y 3 en y

    def update(self): #actualizacion dela velocidad
        self.x += self.speed_x
        self.y += self.speed_y

        # Para rebotar en los bordes de la pantalla
        if self.x <= self.radius or self.x >= WIDTH - self.radius:
            self.speed_x *= -1
        if self.y <= self.radius or self.y >= HEIGHT - self.radius:
            self.speed_y *= -1

    def draw(self, screen): #dibujar
        pygame.draw.circle(screen, CELESTE, (self.x, self.y), self.radius)

# Crear la pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pelotitas rebotando")

#inicializando pelotas
balls = []

# Crear las pelotas con diferentes radios
r = 100
balls.append(Ball(random.randint(r, WIDTH - r), random.randint(r, HEIGHT - r), r))
balls.append(Ball(random.randint(r, WIDTH - r), random.randint(r, HEIGHT - r), r // 2))
balls.append(Ball(random.randint(r, WIDTH - r), random.randint(r, HEIGHT - r), r // 4))
balls.append(Ball(random.randint(r, WIDTH - r), random.randint(r, HEIGHT - r), r // 8))

# Bucle principal del juego
running = True
clock = pygame.time.Clock()

while running:
    # Para controlar los eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar y dibujar las pelotas
    screen.fill(BLACK)
    for ball in balls:
        ball.update()
        ball.draw(screen)

    # Colisión entre pelotas
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            dx = balls[i].x - balls[j].x
            dy = balls[i].y - balls[j].y
            distance = ((dx ** 2) + (dy ** 2)) ** 0.5

            if distance < balls[i].radius + balls[j].radius:
                if balls[i].radius > balls[j].radius / 2:
                    balls[i].radius //= 2
                    balls[j].radius //= 2
                else:
                    balls.pop(j)

    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(60)

# Salir
pygame.quit()