import pygame
import random

class Bonus():
    def __init__(self, ai_game, msg):
        """Инициализирует атрибуты бонуса."""
        self.stats = ai_game.stats
        self.rocket = ai_game.rocket
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.property = random.choice(ai_game.settings.bonus_property)

        # Назначение размеров и свойств бонуса.
        self.width, self.height = 200, 50
        self.button_color = (87, 197, 82)
        self.font = pygame.font.SysFont(None, 48)

        # Построение объекта rect кнопки и выравнивание по центру экрана.
        self.circle = pygame.Circle(0, 0, self.width, self.height)
        self.circle.center = self.screen_rect.center

        # Сообщение кнопки создается только один раз.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Преобразует msg в прямоугольник и выравнивает текст по центру."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.circle.center

    def draw_bonus(self):
        """Отображает бонус"""
        self.screen.fill(self.button_color, self.circle)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def claim_bonus(self):
        '''Применяет бонус к кораблю.'''
        if self.property == 'life':
            self.stats.life_count += 1
        elif self.property == 'speed_low':
            self.settings.rocket_speed = 0.4
        elif self.property == 'speed_high':
            self.settings.rocket_speed = 2
        elif self.property == 'protection':
            self.rocket.protected = True
