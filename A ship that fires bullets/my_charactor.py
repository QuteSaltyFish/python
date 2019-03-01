import pygame


class Badge():
    def __init__(self, screen):
        """Initialize the people and set its starting position."""
        self.screen = screen

        # load the people image and get its rect.
        self.image = pygame.image.load('images/cmu.jpeg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at the middle center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
