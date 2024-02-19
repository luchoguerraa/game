import pygame
import sys
from sprites.ship import Ship
from shared.globalconstant import width_scene, height_scene

# Inicializar Pygame
pygame.init()

window = pygame.display.set_mode((width_scene, height_scene))
pygame.display.set_caption("Mi Primer Juego con Pygame")

# Cargar las imágenes de fondo

background_images = [
    pygame.image.load(f"images/scene{i}.png") for i in range(1, 5)
]
current_background_index = 0
current_background = background_images[current_background_index]
background_rect = current_background.get_rect()

def change_background():
    global current_background_index, current_background
    current_background_index = (current_background_index + 1) % len(background_images)
    current_background = background_images[current_background_index]

# Cargar las imágenes de fondo
#background_image1 = pygame.image.load("images/background1.jpeg")
#background_image2 = pygame.image.load("images/background2.jpeg")
#current_background = background_image1  # Inicializar con la primera imagen
#background_rect = current_background.get_rect()

# Crear una instancia del sprite
moving_object = Ship()

# Crear un grupo de sprites y agregar el objeto
all_sprites = pygame.sprite.Group()
all_sprites.add(moving_object)

# Bucle principal
clock = pygame.time.Clock()
print('Bucle principal')

while True:
    for event in pygame.event.get():
        print('for ->', event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Verificar teclas presionadas
            moving_object.move(event.key)
            if event.key == pygame.K_LEFT:
                moving_object.vel_x = -5
            elif event.key == pygame.K_RIGHT:
                moving_object.vel_x = 5
               
            elif event.key == pygame.K_UP:
                moving_object.vel_y = -5
             
            elif event.key == pygame.K_DOWN:
                moving_object.vel_y = 5
                #moving_object.move(event.key)
            elif event.key == pygame.K_a:
                # Cambiar a la siguiente imagen de fondo
                change_background()
        elif event.type == pygame.KEYUP:
            # Detener el movimiento al soltar las teclas
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                moving_object.vel_x = 0
            elif event.key in [pygame.K_UP, pygame.K_DOWN]:
                moving_object.vel_y = 0


    change_background()
    # Actualizar lógica del juego
    all_sprites.update()

    # Dibujar el fondo
    window.blit(current_background, background_rect)

    # Dibujar los sprites
    all_sprites.draw(window)

    pygame.display.flip()

    # Controlar la velocidad del bucle
    clock.tick(60)
