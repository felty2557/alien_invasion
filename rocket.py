import pygame

from bullet import Bullet


class Rocket:
    """Класс для управления кораблем."""

    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.bonus = None

        # Загружает изображение корабля и получает прямоугольник.
        image = pygame.image.load("images/rocket.png")
        self.image = pygame.transform.scale(image, (self.settings.rocket_width, self.settings.rocket_height))
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

        # Флаги перемещения корабля
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

        # Остальные флаги
        self.protected = False

        # Создается пустой список пуль, который будет заполняться при стрельбе
        self.bullets = pygame.sprite.Group()

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """движение направо и налево"""
        if self.move_right and self.rect.x < (
            self.settings.screen_width - self.settings.rocket_width
        ):
            self.rect.x += self.settings.rocket_speed
        if self.move_left and self.rect.x > 0:
            self.rect.x -= self.settings.rocket_speed
        if self.move_down and self.rect.y < (
            self.settings.screen_height - self.settings.rocket_height
        ):
            self.rect.y += self.settings.rocket_speed
        if self.move_up and self.rect.y > 0:
            self.rect.y -= self.settings.rocket_speed

    def fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def catch_events(self, event):
        """метод отслеживания нажатия кнопок движения и стрельбы коробля."""
        # Стрельба
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.fire_bullet()

        # Передвижение вправо влево
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.move_left = event.type == pygame.KEYDOWN
            elif event.key == pygame.K_RIGHT:
                self.move_right = event.type == pygame.KEYDOWN
            elif event.key == pygame.K_UP:
                self.move_up = event.type == pygame.KEYDOWN
            elif event.key == pygame.K_DOWN:
                self.move_down = event.type == pygame.KEYDOWN
                
    def center_ship(self):
        """Размещает корабль в центре нижней стороны."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
