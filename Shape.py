from vector2 import Vector2
import pygame
class Shape(object)
    def __init__(self, surface):
        self.surface = surface
    
    def draw_goal(self, pos):
        pygame.draw.rect(surface, (0, 255, 0), (pos.x_pos, pos.y_pos, 100, 100))
    def draw_start(self, pos):
        pygame.draw.rect(surface, (0,0,255), (pos.x_pos, pos,y_pos, 100, 100))
    def draw_line(self, pos):
        pygame.draw.line(surface, (0,0,255),pos.x_pos, pos.y_pos)
    def draw_circle(self, pos):
        pygame.draw.circle(surface, (255,0,0), 10)


