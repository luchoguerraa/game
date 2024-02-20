import pygame

class HandlerScene:
    def __init__(self):
        # Cargar las imágenes de fondo
        self.background_images = [
            pygame.image.load(f"images/scene{i}.png") for i in range(1, 5)
        ]

        self.current_background_index = 0
        self.current_background = self.background_images[self.current_background_index]
        self.background_rect = self.current_background.get_rect()

    async def change_background(self):
        self.current_background_index = (self.current_background_index + 1) % len(self.background_images)
        self.current_background = self.background_images[self.current_background_index]

