import pygame


class Alien(pygame.sprite.Sprite):
    """Класс, представляющий одного пришельца."""

    def __init__(self, ai_game):
        """Инициализирует пришельца и задает его начальную позицию."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Загрузка изображения пришельца и назначение атрибута rect.
        self.image = pygame.image.load("images/enemy.png")
        self.image = pygame.transform.scale(self.image, (self.settings.alien_width, self.settings.alien_height))
        
        # Каждый новый пришелец появляется в левом верхнем углу экрана.
        self.rect = self.image.get_rect()
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
        """ Перемещает пришельца по вертикали """
        self.y += self.settings.alien_speed_y
        self.rect.y = self.y

    def update(self):
        """ Перемещает пришельца вправо """
        self.move_x()
        self.move_y()

    @staticmethod
    def create_fleet(ai_game):
        """ 
            Создает флот пришельцев
            Создание пришельца и вычисление количества пришельцев в ряду
            Интервал между соседними пришельцами равен ширине пришельца.
        """
        available_space_x = ai_game.settings.screen_width - (
            2 * ai_game.settings.alien_width
        )
        available_space_y = (
            ai_game.settings.screen_height
            - (3 * ai_game.settings.alien_height)
            - ai_game.rocket.rect.height
        )
        number_aliens_x = available_space_x // (2 * ai_game.settings.alien_width)
        number_aliens_y = available_space_y // (2 * ai_game.settings.alien_height)
        # Создание первого ряда пришельцев.
        for row_number in range(number_aliens_y):
            for alien_number in range(number_aliens_x):
                Alien.create_alien(ai_game, alien_number, row_number)

    @staticmethod
    def create_alien(ai_game, alien_number: int, row_number: int):
        """Создание пришельца и размещение его в ряду."""
        alien = Alien(ai_game)
        alien.x = alien.rect.width + 2 * alien.rect.width * alien_number
        alien.rect.x = alien.x

        alien.y = alien.rect.height + 2 * alien.rect.height * row_number
        alien.rect.y = alien.y
        ai_game.aliens.add(alien)
