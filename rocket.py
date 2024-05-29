import pygame
from bullet import Bullet

class Rocket():
    """Класс для управления кораблем."""
    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # Загружает изображение корабля и получает прямоугольник.
        self.bullets = pygame.sprite.Group()
        image = pygame.image.load('images/rocket.png')
        self.width = 80
        self.height = 120
        self.image = pygame.transform.scale(image, (self.width, self.height))
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
        self.fire = False

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''движение направо и налево'''
        if self.move_right and self.rect.x < (self.settings.screen_width - self.width):
            self.rect.x += self.settings.rocket_speed
        if self.move_left and self.rect.x > 0:
            self.rect.x -= self.settings.rocket_speed
        if self.move_down and self.rect.y < (self.settings.screen_height - self.height):
            self.rect.y += self.settings.rocket_speed
        if self.move_up and self.rect.y > 0:
            self.rect.y -= self.settings.rocket_speed
    
    def fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)