from pygame.sprite import Sprite
import pygame

class Alien(Sprite):
    """Класс вражеского корабля."""
    def __init__(self, ai_game):
        """Инициализирует вражеский корабль и задает его начальную позицию."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # Загружает изображение корабля и получает прямоугольник.
        image = pygame.image.load('images/enemy.png')
        self.width = 80
        self.height = 90
        self.image = pygame.transform.scale(image, (self.width, self.height))
        self.rect = self.image.get_rect()

