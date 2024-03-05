import pygame

class Scene_four:
    def __init__(self):
        # Cargar las imágenes de fondo
        self.background_images = [
            pygame.image.load(f"images/scene4.png") for i in range(1, 5)
        ]

        self.current_background_index = 0
        self.current_background = self.background_images[self.current_background_index]
        self.background_rect = self.current_background.get_rect()

