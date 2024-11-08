import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        self.position = pygame.Vector2(x,y)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", center=(int(self.position.x), int(self.position.y)), radius=self.radius, width=2)
    
    def update(self,dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            print("spawning splits")
            random_angle = random.uniform(20, 50)
            split_1 = self.velocity.rotate(random_angle)
            split_2 = self.velocity.rotate(-random_angle)
            new_size = self.radius - ASTEROID_MIN_RADIUS
            asteroid = Asteroid(self.position.x, self.position.y, new_size)
            asteroid.velocity = split_1 * 1.2
            asteroid = Asteroid(self.position.x, self.position.y, new_size)
            asteroid.velocity = split_2 * 1.2