import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс, представляющий одного пришельца."""
    def __init__(self, ai_game):
        """Инициализирует пришельца и задает его начальную позицию."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Загрузка изображения пришельца и назначение атрибута rect.
        self.image = pygame.image.load('images/enemy.png')
        self.image_width = 80
        self.image_height = 90
        self.image = pygame.transform.scale(self.image, (self.image_width, self.image_height))
        self.rect = self.image.get_rect()
        # Каждый новый пришелец появляется в левом верхнем углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Сохранение точной горизонтальной позиции пришельца.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.go_to_the_left = False
        self.steps = 0
    
    def move_x(self):
        """Перемещает пришельца по горизонтали."""
        if self.go_to_the_left:
            self.x -= self.settings.alien_speed_x
        else:
            self.x += self.settings.alien_speed_x

        self.steps += 1
        if self.steps >= self.settings.alien_max_steps_x:
            self.go_to_the_left = not self.go_to_the_left
            self.steps = 0
        
        self.rect.x = self.x

    def move_y(self):
        """Перемещает пришельца по вертикали."""
        self.y += self.settings.alien_speed_y
        self.rect.y = self.y

    def update(self):
        """Перемещает пришельца вправо."""
        self.move_x()
        self.move_y()
