import pygame

class ScoreBoard():
    """считает очки"""
    def __init__(self, ai_game):
        """Инициализирует подсчет очков."""
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.stats = ai_game.stats
        self.text_color = (255, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        self.msg_image_rect = self.screen.get_rect()
        self.prep_score()
    
    def prep_score(self):
        """задает параметры текста о счете"""
        text = f"очки: {self.stats.score} жизни: {self.stats.life_count}"
        self.msg_image = self.font.render(text, True, self.text_color, self.settings.bg_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.left = 20
        self.msg_image_rect.top = 20

    def show_score(self):
        """выводит значения счета"""
        self.screen.blit(self.msg_image, self.msg_image_rect)
