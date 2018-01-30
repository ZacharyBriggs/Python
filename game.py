#pylint: disable=E1101
import pygame
from vector2 import Vector2
def main():
    pygame.init()
    screen = pygame.display.set_mode((1080, 720))
    screen.fill((255, 100, 100))
    pos = Vector2(100, 100)

    while True:
        if pygame.key.get_pressed()[pygame.K_w] != 0:
            pos.y_pos += 100
        for event in pygame.event.get():
            pygame.draw.rect(screen, (0, 0, 255), (100, 100, pos.x_pos, pos.y_pos))
            if event.type == pygame.QUIT:
                return
            pygame.display.flip()

main()