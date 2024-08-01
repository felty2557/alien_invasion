class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (137, 207, 240)

        # Параметры рокеты
        self.rocket_width = 80
        self.rocket_height = 120
        self.rocket_speed = 1

        # Параметры пули
        self.bullet_width = 10
        self.bullet_height = 30
        self.bullet_speed = 1
        self.bullet_color = (255, 165, 0)

        # Параметры пришельцев
        self.alien_width = 80
        self.alien_height = 90
        self.alien_speed_x = 0.1 # скорость по вертикали
        self.alien_speed_y = 0.05 # скорость по горизонтали
        self.alien_max_steps_x = 100 # амплитуда перемещения пришельца по горизонтали(право-влево)

        self.life_count = 3

        # параметры бонусов
        self.bonus_property = ['speed_low', 'speed_high', 'protection', 'life']
        self.iterations_per_bonus = 2200
        self.iterations_delete_bonus = 1100
        self.bonus_speed_y = 1
        self.bonus_width = 60
        self.bonus_height = 70
