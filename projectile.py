import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius=SHOT_RADIUS):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 1)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color=(255,255,255), center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)