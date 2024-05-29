import sys
from settings import Settings
from rocket import Rocket
import pygame
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
        Alien.create_fleet(self)

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
            for (
                event
            ) in pygame.event.get():  # проходим по всем событиям за момент времени
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

            self.update_objects_positions()
            self.update_screen()

            # удаление всех вражеских кораблей, в которых попала пуля:
            pygame.sprite.groupcollide(self.rocket.bullets, self.aliens, True, True)

    def update_objects_positions(self):
        """Вызываются методы передвижения для всех существующих объектов игры"""
        self.rocket.update()
        self.rocket.bullets.update()
        self.aliens.update()

    def update_screen(self):
        """Обновление экрана c учетом передвижения всех объектов игры"""
        self.screen.fill(self.settings.bg_color)
        # Отображение последнего прорисованного экрана.
        for bullet in self.rocket.bullets:
            bullet.draw()
        self.aliens.draw(self.screen)
        self.rocket.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    # Создание экземпляра и запуск игры
    ai = AlienInvasion()
    # Процессом игры управляет метод run_game(). Метод содержит непрерывно выпол-
    # няемый цикл while, который содержит цикл событий и код, управляющий об-
    # новлениями экрана.
    ai.run_game()
