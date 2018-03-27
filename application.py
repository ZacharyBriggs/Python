from vector2 import Vector2
from graph import Graph
from astar import A_Star
from shape import Rectangle
from shape import Lines
from visual_node import Visual_Node
from visual_graph import Visual_Graph
from visual_astar import Visual_Astar
import pygame

class Application(object):
    def main(self):
        pygame.init()
        screen = pygame.display.set_mode((1080, 720))        
        running = True
        vis_star = Visual_Astar(screen)
        while running:
            screen.fill((0, 0, 0))
            events = pygame.event.get()
            for event in events:
                if event == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE] != 0:
                    running = False 
                vis_star.update()
                vis_star.draw()        
                pygame.display.flip()
                pygame.display.update()

app = Application()
app.main()