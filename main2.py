import pygame
import sys

pygame.init()

# Configurar la ventana
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Escena en movimiento")

# Configurar el reloj
clock = pygame.time.Clock()

# Coordenadas iniciales de la escena
x = 0
y = 0

# Velocidades de movimiento en píxeles por iteración
speed_x = -5
speed_y = -3

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizar las coordenadas de la escena
    x += speed_x
    y += speed_y

    # Limpiar la pantalla
    window.fill((255, 255, 255))

    # Dibujar elementos de la escena (aquí puedes dibujar tus objetos)
    pygame.draw.rect(window, (0, 0, 255), (x, y, 50, 50))  # Ejemplo: un rectángulo azul

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    clock.tick(60)