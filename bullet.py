import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, rocket):
        super().__init__()
        self.screen = rocket.screen
        self.settings = rocket.settings

        self.rect = pygame.Rect(
            0, 0, # начальные координаты, потом сразу изменяются на координаты корабля
            self.settings.bullet_width, # ширина
            self.settings.bullet_height # длина пули
        )
        self.rect.midtop = rocket.rect.midtop # пуля перемещается на место корабля
        self.y = self.rect.y # сохраняется позиция по вертикали, чтобы двигать пулю вверх

    def update(self):
        """ Движение пули вверх """
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw(self):
        """ Вывод снаряда на экран """
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)
