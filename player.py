import pygame
from circleshape import CircleShape
from projectile import Shot
from constants import *

class Player(CircleShape):

    def __init__(self, x, y, radius=PLAYER_RADIUS):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        self.rotation = 0
        self.timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(surface=screen, color=(255, 255, 255), points=self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        bullet = Shot(self.x, self.y, radius=SHOT_RADIUS)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        bullet.velocity = PLAYER_SHOOT_SPEED * pygame.Vector2(0, 1).rotate(self.rotation)
        bullet.position += forward * PLAYER_SHOOT_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot(dt)
                self.timer = PLAYER_SHOOT_TIMER

        self.timer -= dt