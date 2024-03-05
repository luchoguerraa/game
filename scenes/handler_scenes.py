import pygame
from scenes.scenes_1.scene_one import Scene_one
from scenes.scenes_2.scene_two import Scene_two
from scenes.scenes_3.scene_three import Scene_three
from scenes.scenes_4.scene_four import Scene_four

class HandlerScene:
    def __init__(self):
        # Cargar las imágenes de fondo
        self.background_images = [
            pygame.image.load(f"images/scene{i}.png") for i in range(1, 5)
        ]

        # Carga la primera imagen : la numero 0
        self.current_background_index = 0
        self.current_background = self.background_images[self.current_background_index] # define la imagen
        self.background_rect = self.current_background.get_rect() # define la dimencion del rectangulo

        # Crear instancias de las clases Scene_one, Scene_two, Scene_three, Scene_four y guardarlas en un array
        self.scenes = [Scene_one(), Scene_two(), Scene_three(), Scene_four()]

    async def change_background(self):
        self.current_background_index = (self.current_background_index + 1) % len(self.background_images)
        self.current_background = self.background_images[self.current_background_index]
    
    async def change_background2(self):
        self.current_background_index = (self.current_background_index + 1) % len(self.background_images)
        self.current_background = self.scenes[self.current_background_index].current_background
               
