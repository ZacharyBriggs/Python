#pylint: disable=E1101
import pygame
from vector2 import Vector2
def main():
    pygame.init()
    screen = pygame.display.set_mode((1080, 720))
    screen.fill((255, 100, 100))
    pos = Vector2(100, 100)
    pygame.key.set_repeat(1, 1)
    while True:
        if pygame.key.get_pressed()[pygame.K_w] != 0:
            pos.y_pos -= .15
        if pygame.key.get_pressed()[pygame.K_s] != 0:
            pos.y_pos += .15
        if pygame.key.get_pressed()[pygame.K_a] != 0:
            pos.x_pos -= .15
        if pygame.key.get_pressed()[pygame.K_d] != 0:
            pos.x_pos += .15
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            pygame.draw.rect(screen, (0, 0, 255), (pos.x_pos, pos.y_pos, 100, 100))
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE] != 0:
                return
            pygame.display.flip()
main()