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
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.create_game_objects()

    def create_game_objects(self):
        # Создание всех объектов игры
        self.aliens = pygame.sprite.Group()
        self.rocket = Rocket(self)
        self.create_fleet()

    def run_game(self):
        """
            Запуск основного цикла игры.
            Сюда нужно помещать действия, которые нужно выполнять непрерывно.
            Например: 
            1. Обрабатывать все действия пользователя
            2. Вызывать методы передвижения объектов игры
        """
        while True:
            # Отслеживание событий клавиатуры и мыши.
            for event in pygame.event.get(): # проходим по всем событиям за момент времени
                # Если клик на кнопке закрытия игрового поля
                # или если нажали клавишу Q
                if event.type == pygame.QUIT \
                or event.type == pygame.KEYDOWN and event.key == pygame.K_q:  
                    sys.exit() # Закрыть окно с игрой

                self.catch_rocket_events(event) # вызов 

            self.update_objects_positions()
            self.update_screen()

            # удаление всех вражеских кораблей, в которых попала пуля:
            pygame.sprite.groupcollide(self.rocket.bullets, self.aliens, True, True)

    def update_objects_positions(self):
        """ Вызываются методы передвижения для всех существующих объектов игры """       
        self.rocket.update()
        self.rocket.bullets.update()
        self.aliens.update()

    def catch_rocket_events(self, event):
        """ метод отслеживания нажатия кнопок движения и стрельбы коробля."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.rocket.fire = True
                self.rocket.fire_bullet()
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

    def update_screen(self):
        """Обновление экрана"""
        self.screen.fill(self.settings.bg_color)
        # Отображение последнего прорисованного экрана.
        for bullet in self.rocket.bullets:
            bullet.draw()
        self.aliens.draw(self.screen)
        self.rocket.blitme()
        pygame.display.flip()

    def create_fleet(self):
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
                self.create_alien(alien_number, row_number)

    def create_alien(self, alien_number: int, row_number: int):
        """Создание пришельца и размещение его в ряду."""
        alien = Alien(self)
        alien.x = alien.rect.width + 2 * alien.rect.width * alien_number
        alien.rect.x = alien.x

        alien.y = alien.rect.height + 2 * alien.rect.height * row_number
        alien.rect.y = alien.y
        self.aliens.add(alien)


if __name__ == "__main__":
    # Создание экземпляра и запуск игры
    ai = AlienInvasion()
    # Процессом игры управляет метод run_game(). Метод содержит непрерывно выпол-
    # няемый цикл while, который содержит цикл событий и код, управляющий об-
    # новлениями экрана.
    ai.run_game()
