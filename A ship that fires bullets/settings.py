class Settings():
    """A class to store all setting for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 2

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien sttings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speed_up_scale = 1.1
        # How quicklt the alien point values increase
        self.score_scale = 1.5
        self.initialize_dynaimc_settings()

    def initialize_dynaimc_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # Fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speed_up_scale
        self.bullet_speed_factor *= self.speed_up_scale
        self.alien_speed_factor *= self.speed_up_scale

        self.alien_points = int(self.alien_points * self.alien_speed_factor)
        print(self.alien_points)
