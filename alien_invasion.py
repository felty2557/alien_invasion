import sys
import pygame

from alien import Alien
from rocket import Rocket
from settings import Settings
from game_stats import GameStats
from time import sleep
from button import Button


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()

        self.settings = Settings()
        self.stats = GameStats(self)
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.create_game_objects()

    def create_game_objects(self):
        """ Создание всех объектов игры """
        self.aliens = pygame.sprite.Group()
        self.rocket = Rocket(self)
        Alien.create_fleet(self)
        self.play_button = Button(self, "play")

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
            for event in pygame.event.get():  # проходим по всем событиям за момент времени
                # Если клик на кнопке закрытия игрового поля
                # или если нажали клавишу Q
                if (
                    event.type == pygame.QUIT
                    or event.type == pygame.KEYDOWN
                    and event.key == pygame.K_q
                ):
                    sys.exit()  # Закрыть окно с игрой

                # вызов отлавливания события нажатия кнопок вправо-влево
                # для передвижения корабля
                self.rocket.catch_events(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self._check_play_button(pygame.mouse.get_pos())

            self.update_objects_positions()
            self.update_screen()

            # удаление всех вражеских кораблей, в которых попала пуля:
            pygame.sprite.groupcollide(self.rocket.bullets, self.aliens, True, True)
            if pygame.sprite.spritecollideany(self.rocket, self.aliens):
                self.rocket_hit()

    def rocket_hit(self):
        """Обрабатывает столкновение корабля с пришельцем."""
        # Уменьшение ships_left.
        self.stats.life_count -= 1

        # Очистка списков пришельцев и снарядов.
        self.aliens.empty()
        self.rocket.bullets.empty()

        # Создание нового флота и размещение корабля в центре.
        Alien.create_fleet(self)
        self.rocket.center_ship()

        # приостанавливаем игру, если количество жизней дошло до нуля
        if self.stats.life_count <= 0:
            self.stats.game_active = False

        # Пауза.
        sleep(0.5)

    def update_objects_positions(self):
        """Вызываются методы передвижения для всех существующих объектов игры"""
        if self.stats.game_active:
            self.rocket.update()
            self.rocket.bullets.update()
            self.aliens.update()

    def _check_play_button(self, mouse_pos):
        """При нажатии на кнопку play активирует игру"""
        if self.play_button.rect.collidepoint(mouse_pos):
            self.stats.game_active = True

    def update_screen(self):
        """Обновление экрана c учетом передвижения всех объектов игры"""
        self.screen.fill(self.settings.bg_color)
        # Отображение последнего прорисованного экрана.
        for bullet in self.rocket.bullets:
            bullet.draw()
        self.aliens.draw(self.screen)
        if not self.stats.game_active:
            self.play_button.draw_button()
        self.rocket.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    # Создание экземпляра и запуск игры
    ai = AlienInvasion()
    # Процессом игры управляет метод run_game(). Метод содержит непрерывно выпол-
    # няемый цикл while, который содержит цикл событий и код, управляющий об-
    # новлениями экрана.
    ai.run_game()
