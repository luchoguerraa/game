import pygame
import sys
import asyncio  # Agrega esta línea
from sprites.ship import Ship
from shared.globalconstant import width_scene, height_scene
from scenes.handler_scenes import HandlerScene
# Inicializar Pygame
pygame.init()

window = pygame.display.set_mode((width_scene, height_scene))
pygame.display.set_caption("space attack")

# defined the scene
handler_scene = HandlerScene()

current_background_index = 0
current_background = handler_scene.background_images[current_background_index]
background_rect = current_background.get_rect()

# Crear una instancia del sprite
moving_object = Ship()

# Crear un grupo de sprites y agregar el objeto
all_sprites = pygame.sprite.Group()
all_sprites.add(moving_object)

# Bucle principal
clock = pygame.time.Clock()

async def main_loop():

    while True:
        for event in pygame.event.get():
         
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                moving_object.move(event.key)
                if event.key == pygame.K_LEFT:
                    moving_object.vel_x = -5
                elif event.key == pygame.K_RIGHT:
                    moving_object.vel_x = 5
                elif event.key == pygame.K_UP:
                    moving_object.vel_y = -5
                elif event.key == pygame.K_DOWN:
                    moving_object.vel_y = 5
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    moving_object.vel_x = 0
                elif event.key in [pygame.K_UP, pygame.K_DOWN]:
                    moving_object.vel_y = 0

            
        await handler_scene.change_background()
        # Actualizar lógica del juego
        all_sprites.update()

        # Dibujar el fondo
        window.blit(handler_scene.current_background, handler_scene.background_rect)

        # Dibujar los sprites
        all_sprites.draw(window)

        pygame.display.flip()

        # Controlar la velocidad del bucle
        clock.tick(60)

# Ejecutar el bucle principal
pygame.event.pump()
pygame.display.flip()
pygame.key.set_repeat(1, 1)

# Ejecutar el bucle principal de forma asíncrona
asyncio.run(main_loop())
