import pygame
import random

from random import randrange

class Bonus():
    def __init__(self, ai_game):
        """Инициализирует атрибуты бонуса."""
        self.stats = ai_game.stats
        self.rocket = ai_game.rocket
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.property = random.choice(ai_game.settings.bonus_property)
        self.x = randrange(ai_game.settings.screen_width)
        
        # Загрузка изображения бонуса.
        self.image = pygame.image.load(f"images/{self.property}_bonus.svg")
        self.image = pygame.transform.scale(self.image, (self.settings.bonus_width, self.settings.bonus_height))
        
        # Каждый новый бонус появляется в любой позиции наверху.
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.x = randrange(ai_game.settings.screen_width)
        self.y = 0
        self.rect.y = self.y

    def blitme(self):
        """Рисует бонус в текущей позиции."""
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        """Перемещает бонус вниз."""
        self.y += self.settings.bonus_speed_y
        self.rect.y = self.y

    def claim_bonus(self):
        '''Применяет бонус к кораблю.'''
        if self.property == 'life':
            self.stats.life_count += 1
        elif self.property == 'speed_low':
            self.settings.rocket_speed = 1
        elif self.property == 'speed_high':
            self.settings.rocket_speed = 3
        elif self.property == "protection":
            self.rocket.protected = True

    def reclaim_bonus(self):
        '''Отменяет бонус к кораблю.'''
        self.settings.rocket_speed = 1
        self.rocket.protected = False