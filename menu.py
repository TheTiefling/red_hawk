import pygame

class Menu:
    def __init__(self):
        self.is_active = True
        self.font = pygame.font.Font(None, 48)
        self.title_text = self.font.render("Red Hawlk - Space Invaders", True, (255, 255, 255))
        self.start_text = self.font.render("Press Enter to Start", True, (255, 255, 255))
        self.quit_text = self.font.render("Press ESC to Quit", True, (255, 255, 255))
    
    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.is_active = False
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
    
    def update(self):
        pass
    
    def draw(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.title_text, (175, 100))
        screen.blit(self.start_text, (250, 250))
        screen.blit(self.quit_text, (265, 300))

