from pygame.sprite import Sprite
import pygame

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        self.rect.midtop = ai_game.rocket.rect.midtop
        self.y = self.rect.y

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Вывод снаряда на экран."""
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)

