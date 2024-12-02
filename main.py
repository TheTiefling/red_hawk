import pygame
from scenes import GameScene
from menu import Menu

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Red Hawk")

def main():
    clock = pygame.time.Clock()
    
    menu = Menu()
    game_scene = None
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  
            if menu.is_active:
                menu.handle_events(event)
            elif game_scene:
                game_scene.handle_events(event)
        if menu.is_active:
            menu.update()
            menu.draw(screen)
        else:
            if game_scene is None:
                game_scene = GameScene(level=1)
            game_scene.update()
            game_scene.draw(screen)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()
 