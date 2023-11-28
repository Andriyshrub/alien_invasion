import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс представляюший одного пришельца"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # Загрузка изображения пришельца и задает первоночальную позицию
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появлется в (0, 0)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Создание точки горизнотальной позиции пришельца
        self.x = float(self.rect.x)
