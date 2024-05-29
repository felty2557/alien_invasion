import sys
from settings import Settings
from rocket import Rocket
import pygame  # Модуль pygame содержит функциональность, необходимую для создания игры
from bullet import Bullet
import time
from alien import Alien


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (0, 0), pygame.FULLSCREEN
        )  # создает окно c указанными
        # размерами - возвращает игровое поле
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            # Отслеживание событий клавиатуры и мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # кнопка закрытия игрового поля
                    sys.exit()

                self.catch_event_move(event)
            self.rocket.move()
            self.bullets.update()
            self.aliens.update()
            pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
            self._update_screen()

    def catch_event_move(self, event):
        """отслеживания нажатия кнопок движения коробля."""

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.rocket.fire = True
                self._fire_bullet()
            if event.key == pygame.K_e:
                sys.exit()
            if event.key == pygame.K_LEFT:
                self.rocket.move_left = True
            elif event.key == pygame.K_RIGHT:
                self.rocket.move_right = True
            elif event.key == pygame.K_UP:
                self.rocket.move_up = True
            elif event.key == pygame.K_DOWN:
                self.rocket.move_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.rocket.fire = False
            if event.key == pygame.K_LEFT:
                self.rocket.move_left = False
            elif event.key == pygame.K_RIGHT:
                self.rocket.move_right = False
            elif event.key == pygame.K_UP:
                self.rocket.move_up = False
            elif event.key == pygame.K_DOWN:
                self.rocket.move_down = False

    def _update_screen(self):
        """обновление экрана."""
        self.screen.fill(self.settings.bg_color)
        # Отображение последнего прорисованного экрана.
        for bulleta in self.bullets:
            bulleta.draw_bullet()
        self.aliens.draw(self.screen)
        self.rocket.blitme()
        pygame.display.flip()

    def fire_bullet(self):
        if self.rocket.fire:
            self.bullets.add(Bullet(self))
            time.sleep(0.2)

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _create_fleet(self):
        """Создает флот пришельцев."""
        # Создание пришельца и вычисление количества пришельцев в ряду
        # Интервал между соседними пришельцами равен ширине пришельца.
        available_space_x = self.settings.screen_width - (2 * self.settings.alien_width)
        available_space_y = (
            self.settings.screen_height
            - (3 * self.settings.alien_height)
            - self.rocket.rect.height
        )
        number_aliens_x = available_space_x // (2 * self.settings.alien_width)
        number_aliens_y = available_space_y // (2 * self.settings.alien_height)
        # Создание первого ряда пришельцев.
        for row_number in range(number_aliens_y):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number: int, row_number: int):
        """Создание пришельца и размещение его в ряду."""
        alien = Alien(self)
        alien.x = alien.rect.width + 2 * alien.rect.width * alien_number
        alien.rect.x = alien.x

        alien.y = alien.rect.height + 2 * alien.rect.height * row_number
        alien.rect.y = alien.y
        self.aliens.add(alien)


if __name__ == "__main__":
    # Создание экземпляра и запуск игры.н
    ai = AlienInvasion()
    # Процессом игры управляет метод run_game(). Метод содержит непрерывно выпол-
    # няемый цикл while, который содержит цикл событий и код, управляющий об-
    # новлениями экрана.
    ai.run_game()
