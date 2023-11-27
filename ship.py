import pygame


class Ship():
    """Класс управления кораблем."""

    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Загружаем изображение корабля и получаем прямоугольник.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Каждий новий корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False

        # Сохранение вещественной координаты
        self.x = float(self.rect.x)


    def update(self):
        """Обновляет  позицию корабля с учетом флага"""
        # Обновление атрибута x
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

         #Обновление атрибута rect
        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
