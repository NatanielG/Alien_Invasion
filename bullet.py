import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class to manage bullet fired from the ship"""

    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen

        #Create a bullet rectangle at (0, 0) and set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #Store the bullet position as decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    

    def update(self):
        """Move the bullet up the screen"""
        #Update decimal position of the bullet
        self.y -= self.speed_factor
        #Update the rect position
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Draw bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)