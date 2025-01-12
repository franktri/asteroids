# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from projectile import Shot
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
           
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, (0, 0, 0))

        for update_item in updatable:
            update_item.update(dt)
        for asteroid in asteroids:
            has_collided = asteroid.check_collisions(player)
            if has_collided:
                sys.exit("Game over!")
            else:
                pass
        for asteroid in asteroids:
            for bullet in shots:
                has_collided = asteroid.check_collisions(bullet)
                if has_collided:
                    asteroid.split()
                    bullet.kill()
        for draw_item in drawable:
            draw_item.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()