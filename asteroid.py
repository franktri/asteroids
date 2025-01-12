import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color=(255,255,255), center=self.position, radius=self.radius, width=2)

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(COLLISION_ANGLE_MIN, COLLISION_ANGLE_MAX)
        new_vel_pos = self.velocity.rotate(random_angle)
        new_vel_neg = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_x, asteroid_y = self.position
        asteroid_pos = Asteroid(asteroid_x, asteroid_y, new_radius)
        asteroid_pos.velocity = 1.2*new_vel_pos
        asteroid_neg = Asteroid(asteroid_x, asteroid_y, new_radius)
        asteroid_neg.velocity = 1.2*new_vel_neg

    def update(self, dt):
        self.position += (self.velocity * dt)