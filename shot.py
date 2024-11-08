import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.x = x
        self.y = y
        
        self.position = pygame.Vector2(x,y)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", center=(int(self.position.x), int(self.position.y)), radius=self.radius, width=2)
    
    def update(self,dt):
        self.position += (self.velocity * dt)