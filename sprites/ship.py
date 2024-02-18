import pygame
from shared.globalconstant import width_scene, height_scene

# Crear un sprite para el objeto que se moverá
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # Cargar la imagen del objeto
        self.original_image = pygame.image.load("images/ship.png")  # Ruta de la imagen del objeto
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (width_scene // 2, height_scene // 2)  # Posición inicial
        self.vel_x = 0  # Velocidad en el eje X
        self.vel_y = 0  # Velocidad en el eje Y
        self.angle = 0  # Ángulo de rotación

    def update(self):
        # Actualizar posición basada en la velocidad
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Rotar la imagen
        self.rotate()

        # Si el objeto se sale de la pantalla, reiniciar su posición
        if self.rect.right < 0:
            self.rect.left = width_scene
        if self.rect.left > width_scene:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = height_scene
        if self.rect.top > height_scene:
            self.rect.bottom = 0

    def rotate(self):
        # Rotar la imagen y actualizar el rectángulo
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
